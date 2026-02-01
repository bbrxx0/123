# Диаграмма классов - StayFinder

## Основные классы системы

### 1. User (Пользователь)
**Атрибуты:**
- id: Integer (PK)
- email: String(255) {unique}
- password_hash: String(255)
- is_admin: Boolean
- is_email_confirmed: Boolean
- email_confirmed_at: DateTime
- created_at: DateTime

**Методы:**
- set_password(password: str): void
- check_password(password: str): bool
- confirm_email(): void

---

### 2. Hotel (Отель)
**Атрибуты:**
- id: Integer (PK)
- name: String(180)
- city: String(120)
- address: String(255)
- description: Text
- highlights: Text
- stars: Integer
- image_url: String(500)
- created_at: DateTime

**Методы:**
- (унаследованы от db.Model)

---

### 3. Room (Номер)
**Атрибуты:**
- id: Integer (PK)
- hotel_id: Integer (FK → Hotel.id)
- name: String(180)
- capacity: Integer
- price_per_night: Integer
- description: Text

**Методы:**
- (унаследованы от db.Model)

---

### 4. Reservation (Бронирование)
**Атрибуты:**
- id: Integer (PK)
- user_id: Integer (FK → User.id)
- room_id: Integer (FK → Room.id)
- check_in: Date
- check_out: Date
- status: String(20) {pending/confirmed/canceled}
- payment_status: String(20) {unpaid/paid/refunded/failed}
- stripe_session_id: String(255)
- stripe_payment_intent_id: String(255)
- paid_at: DateTime
- created_at: DateTime

**Методы:**
- nights(): int {property}
- total_price(): int
- mark_paid(session_id: str, payment_intent_id: str): void

---

## Классы форм (Flask-WTF)

### 5. RegisterForm
**Поля:**
- email: StringField
- password: PasswordField
- confirm: PasswordField
- submit: SubmitField

**Методы:**
- validate_email(field): void

---

### 6. LoginForm
**Поля:**
- email: StringField
- password: PasswordField
- remember: BooleanField
- submit: SubmitField

---

### 7. BookingForm
**Поля:**
- check_in: DateField
- check_out: DateField
- submit: SubmitField

**Методы:**
- validate_check_in(field): void
- validate_check_out(field): void

---

### 8. HotelForm
**Поля:**
- name: StringField
- city: StringField
- address: StringField
- stars: IntegerField
- image_url: StringField
- highlights: TextAreaField
- description: TextAreaField
- submit: SubmitField

---

### 9. RoomForm
**Поля:**
- name: StringField
- capacity: IntegerField
- price_per_night: IntegerField
- description: TextAreaField
- submit: SubmitField

---

## Отношения между классами

### Ассоциации (Association)
1. **User ←→ Reservation** (1 к многим)
   - User может иметь много Reservation
   - Reservation принадлежит одному User
   - Кардинальность: 1..* (один пользователь → много бронирований)

2. **Room ←→ Reservation** (1 к многим)
   - Room может иметь много Reservation
   - Reservation связано с одним Room
   - Кардинальность: 1..* (один номер → много бронирований)

### Композиция (Composition)
3. **Hotel ◆—→ Room** (1 к многим)
   - Hotel содержит много Room
   - Room не существует без Hotel
   - Кардинальность: 1..* (один отель → много номеров)
   - При удалении Hotel удаляются все Room (cascade delete)

### Наследование (Inheritance)
4. **User → UserMixin** (наследование)
   - User наследуется от UserMixin (Flask-Login)

5. **User → db.Model** (наследование)
   - User наследуется от db.Model (SQLAlchemy)

6. **Все формы → FlaskForm** (наследование)
   - RegisterForm → FlaskForm
   - LoginForm → FlaskForm
   - BookingForm → FlaskForm
   - HotelForm → FlaskForm
   - RoomForm → FlaskForm

---

## Пошаговая инструкция создания в Visual Paradigm

### Шаг 1: Создание диаграммы классов
1. File → New Diagram
2. Выбрать **UML Structural** → **Class Diagram**
3. Название: **StayFinder Class Diagram**
4. OK

### Шаг 2: Добавление основных классов моделей
1. На панели выбрать **Class**
2. Кликнуть на диаграмму → добавить класс **User**
3. Повторить для классов:
   - **Hotel**
   - **Room**
   - **Reservation**

### Шаг 3: Добавление атрибутов класса User
1. Правый клик на класс **User** → **Add → Attribute**
2. Добавить атрибуты (формат: visibility name: type):
   ```
   - id: Integer
   - email: String
   - password_hash: String
   - is_admin: Boolean
   - is_email_confirmed: Boolean
   - email_confirmed_at: DateTime
   - created_at: DateTime
   ```
3. Для установки видимости:
   - `-` (private) для password_hash
   - `+` (public) для остальных

### Шаг 4: Добавление методов класса User
1. Правый клик на **User** → **Add → Operation**
2. Добавить методы:
   ```
   + set_password(password: String): void
   + check_password(password: String): Boolean
   + confirm_email(): void
   ```

### Шаг 5: Добавление атрибутов для Hotel
Правый клик на **Hotel** → Add → Attribute:
```
+ id: Integer
+ name: String
+ city: String
+ address: String
+ description: String
+ highlights: String
+ stars: Integer
+ image_url: String
+ created_at: DateTime
```

### Шаг 6: Добавление атрибутов для Room
Правый клик на **Room** → Add → Attribute:
```
+ id: Integer
+ hotel_id: Integer
+ name: String
+ capacity: Integer
+ price_per_night: Integer
+ description: String
```

### Шаг 7: Добавление атрибутов для Reservation
Правый клик на **Reservation** → Add → Attribute:
```
+ id: Integer
+ user_id: Integer
+ room_id: Integer
+ check_in: Date
+ check_out: Date
+ status: String
+ payment_status: String
+ stripe_session_id: String
+ stripe_payment_intent_id: String
+ paid_at: DateTime
+ created_at: DateTime
```

Добавить методы:
```
+ nights(): Integer
+ total_price(): Integer
+ mark_paid(session_id: String, payment_intent_id: String): void
```

### Шаг 8: Создание связи User ← Reservation (Ассоциация)
1. На панели выбрать **Association** (линия)
2. Провести от **Reservation** к **User**
3. Двойной клик на линию → Properties
4. Установить:
   - **From End** (Reservation): multiplicity = `*` (многие)
   - **To End** (User): multiplicity = `1` (один)
   - Name: `user`
5. OK

### Шаг 9: Создание связи Room ← Reservation (Ассоциация)
1. Выбрать **Association**
2. Провести от **Reservation** к **Room**
3. Двойной клик → Properties:
   - From End: multiplicity = `*`
   - To End: multiplicity = `1`
   - Name: `room`

### Шаг 10: Создание связи Hotel → Room (Композиция)
1. На панели выбрать **Composition** (линия с закрашенным ромбом)
2. Провести от **Hotel** к **Room**
3. Двойной клик → Properties:
   - From End (Hotel): multiplicity = `1`
   - To End (Room): multiplicity = `1..*` (один или много)
   - Name: `rooms`

### Шаг 11: Добавление классов форм (опционально)
Если нужно показать формы:
1. Создать пакет (Package): **Forms**
2. Добавить классы внутри пакета:
   - **RegisterForm**
   - **LoginForm**
   - **BookingForm**
   - **HotelForm**
   - **RoomForm**

### Шаг 12: Создание наследования FlaskForm
1. Создать класс **FlaskForm** (можно вынести за границу или пометить как external)
2. На панели выбрать **Generalization** (стрелка с незакрашенным треугольником)
3. Провести от **RegisterForm** к **FlaskForm**
4. Повторить для всех форм

### Шаг 13: Добавление стереотипов и пометок
1. Правый клик на атрибут `id` → **Stereotypes**
2. Добавить стереотип: `<<PK>>` (Primary Key)
3. Для внешних ключей добавить: `<<FK>>` (Foreign Key)
   - `hotel_id` в Room
   - `user_id` в Reservation
   - `room_id` в Reservation

### Шаг 14: Форматирование диаграммы
1. Расположить классы логично:
   - **User** (слева вверху)
   - **Reservation** (по центру)
   - **Room** (справа)
   - **Hotel** (справа вверху)
2. Автоматическое выравнивание: **Format → Auto Layout → Hierarchical**
3. Настроить цвета:
   - Модели данных: светло-синий
   - Формы: светло-желтый
4. **File → Export → Active Diagram as Image**
5. Формат: PNG, качество: High

---

## Схема расположения классов

```
┌─────────────┐                              ┌─────────────┐
│    User     │                              │    Hotel    │
├─────────────┤                              ├─────────────┤
│- id         │                              │+ id         │
│+ email      │                              │+ name       │
│- password   │                              │+ city       │
│+ is_admin   │                              │+ stars      │
├─────────────┤                              │+ ...        │
│+ set_pwd()  │                              └──────┬──────┘
│+ check_pwd()│                                     │
└──────┬──────┘                                     │ 1
       │ 1                                          │ 
       │                                            │ rooms
       │                                            ◆ (composition)
       │                                            │
       │                                            │ 1..*
       │                                     ┌──────▼──────┐
       │                                     │    Room     │
       │                                     ├─────────────┤
       │ user                                │+ id         │
       │                                     │+ hotel_id FK│
       │                                     │+ name       │
       │                                     │+ capacity   │
       │ *                                   │+ price      │
┌──────▼──────────┐                         └──────┬──────┘
│  Reservation    │                                │ 1
├─────────────────┤                                │
│+ id             │                                │
│+ user_id FK     │                                │
│+ room_id FK ────┼────────────────────────────────┘ room
│+ check_in       │                                  *
│+ check_out      │
│+ status         │
│+ payment_status │
├─────────────────┤
│+ nights()       │
│+ total_price()  │
│+ mark_paid()    │
└─────────────────┘


         ┌──────────────┐
         │  FlaskForm   │ (базовый класс)
         └───────┬──────┘
                 │
        ┌────────┴─────────────────┬─────────────┬──────────┐
        │                          │             │          │
┌───────▼────────┐      ┌─────────▼──────┐  ┌──▼──────┐ ┌─▼────────┐
│ RegisterForm   │      │  LoginForm     │  │HotelForm│ │RoomForm  │
├────────────────┤      ├────────────────┤  ├─────────┤ ├──────────┤
│+ email         │      │+ email         │  │+ name   │ │+ name    │
│+ password      │      │+ password      │  │+ city   │ │+ capacity│
│+ confirm       │      │+ remember      │  │+ stars  │ │+ price   │
└────────────────┘      └────────────────┘  └─────────┘ └──────────┘
```

---

## Дополнительные элементы (опционально)

### Интерфейсы
Если хочешь показать интерфейсы SQLAlchemy:
1. Создать **Interface**: `<<interface>> db.Model`
2. Связать все классы моделей с этим интерфейсом через **Realization** (пунктирная стрелка)

### Классы-утилиты
Можно добавить служебные функции как отдельный класс:
```
┌─────────────────────┐
│ <<utility>>         │
│ RoomAvailability    │
├─────────────────────┤
│+ room_is_available()│
└─────────────────────┘
```

---

## Советы

1. **Не перегружай диаграмму** - покажи только важные атрибуты
2. **Используй пакеты** - группируй связанные классы (Models, Forms)
3. **Цветовое кодирование**:
   - Модели БД - один цвет
   - Формы - другой цвет
   - Служебные классы - третий цвет
4. **Стереотипы** - используй для пометки специальных элементов (<<PK>>, <<FK>>, <<entity>>)
5. **Мультипликативность** - всегда указывай кардинальность связей (1, *, 0..1, 1..*)

---

## Типичные ошибки

❌ Не показывай геттеры/сеттеры для каждого атрибута  
✅ Покажи только важные бизнес-методы

❌ Не рисуй связи между всеми классами  
✅ Рисуй только прямые связи из кода

❌ Не добавляй служебные атрибуты (timestamps везде)  
✅ Покажи ключевые атрибуты для понимания структуры

❌ Не используй разные стили стрелок произвольно  
✅ Строго соблюдай UML нотацию:
  - Association: простая линия
  - Composition: линия с закрашенным ромбом
  - Aggregation: линия с незакрашенным ромбом
  - Generalization: стрелка с незакрашенным треугольником
  - Realization: пунктирная стрелка с незакрашенным треугольником

---

## Контрольный список

- [ ] Все основные классы добавлены (User, Hotel, Room, Reservation)
- [ ] Атрибуты с правильными типами данных
- [ ] Методы добавлены для классов
- [ ] Связи между классами правильно обозначены
- [ ] Указана кардинальность (1, *, 1..*, 0..1)
- [ ] Primary Keys помечены как PK
- [ ] Foreign Keys помечены как FK
- [ ] Композиция Hotel-Room показана правильно (ромб)
- [ ] Наследование форм от FlaskForm показано
- [ ] Диаграмма читаема и не перегружена
- [ ] Экспортировано в PNG/SVG высокого качества

---

**Готово!** Теперь у тебя есть инструкция для создания диаграммы классов в Visual Paradigm.
