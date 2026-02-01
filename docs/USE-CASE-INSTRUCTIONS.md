# Instrukcja krok po kroku: Diagram przypadków użycia w Visual Paradigm
## Пошаговая инструкция: Диаграмма вариантов использования в Visual Paradigm

---

## 📋 Spis treści / Содержание

1. [Wprowadzenie](#wprowadzenie--введение)
2. [Przygotowanie](#przygotowanie--подготовка)
3. [Tworzenie diagramu](#tworzenie-diagramu--создание-диаграммы)
4. [Eksport i zapisywanie](#eksport-i-zapisywanie--экспорт-и-сохранение)

---

## 🎯 Wprowadzenie / Введение

**PL:** Ten dokument zawiera szczegółową instrukcję tworzenia diagramu przypadków użycia dla systemu rezerwacji hotelowej StayFinder w programie Visual Paradigm.

**RU:** Этот документ содержит подробную инструкцию по созданию диаграммы вариантов использования для системы бронирования отелей StayFinder в программе Visual Paradigm.

---

## 🔧 Przygotowanie / Подготовка

### Krok 1: Zainstaluj Visual Paradigm
**PL:** 
1. Pobierz Visual Paradigm ze strony: https://www.visual-paradigm.com/download/
2. Wybierz wersję Community Edition (darmowa) lub wersję próbną
3. Zainstaluj program według instrukcji instalatora
4. Uruchom Visual Paradigm

**RU:**
1. Скачайте Visual Paradigm с сайта: https://www.visual-paradigm.com/download/
2. Выберите версию Community Edition (бесплатная) или пробную версию
3. Установите программу, следуя инструкциям установщика
4. Запустите Visual Paradigm

### Krok 2: Utwórz nowy projekt
**PL:**
1. W Visual Paradigm kliknij **File → New Project**
2. Wpisz nazwę projektu: "StayFinder"
3. Kliknij **OK**

**RU:**
1. В Visual Paradigm нажмите **File → New Project**
2. Введите имя проекта: "StayFinder"
3. Нажмите **OK**

---

## 🎨 Tworzenie diagramu / Создание диаграммы

### Krok 3: Stwórz diagram przypadków użycia
**PL:**
1. W menu górnym wybierz **Diagram → New**
2. Z listy wybierz **Use Case Diagram**
3. Nadaj nazwę: "StayFinder Use Case Diagram"
4. Kliknij **OK**

**RU:**
1. В верхнем меню выберите **Diagram → New**
2. Из списка выберите **Use Case Diagram**
3. Дайте название: "StayFinder Use Case Diagram"
4. Нажмите **OK**

### Krok 4: Dodaj aktorów (Actors)
**PL:**
Na diagramie przypadków użycia mamy 4 aktorów:

**RU:**
В диаграмме вариантов использования у нас 4 актора:

#### 4.1. Dodaj aktora "Guest" (Gość)
**PL:**
1. W panelu narzędzi po lewej stronie znajdź ikonę **Actor** (ludzik)
2. Kliknij na ikonę, a następnie kliknij na obszar diagramu (lewa strona)
3. Wpisz nazwę: "Guest" lub "Gość"
4. Naciśnij Enter

**RU:**
1. В панели инструментов слева найдите иконку **Actor** (человечек)
2. Щелкните по иконке, затем щелкните на область диаграммы (левая сторона)
3. Введите имя: "Guest" или "Гость"
4. Нажмите Enter

#### 4.2. Dodaj aktora "Registered User" (Zarejestrowany użytkownik)
**PL:**
1. Powtórz kroki jak dla Guest
2. Umieść go poniżej Guest
3. Wpisz nazwę: "Registered User" lub "Zarejestrowany użytkownik"

**RU:**
1. Повторите шаги как для Guest
2. Разместите его ниже Guest
3. Введите имя: "Registered User" или "Зарегистрированный пользователь"

#### 4.3. Dodaj aktora "Administrator"
**PL:**
1. Powtórz kroki
2. Umieść go po lewej dolnej stronie
3. Wpisz nazwę: "Administrator"

**RU:**
1. Повторите шаги
2. Разместите его в левом нижнем углу
3. Введите имя: "Administrator" или "Администратор"

#### 4.4. Dodaj aktora "Stripe Payment System"
**PL:**
1. Powtórz kroki
2. Umieść go po prawej stronie diagramu
3. Wpisz nazwę: "Stripe Payment System" lub "System płatności Stripe"

**RU:**
1. Повторите шаги
2. Разместите его справа на диаграмме
3. Введите имя: "Stripe Payment System" или "Система платежей Stripe"

### Krok 5: Dodaj granicę systemu (System Boundary)
**PL:**
1. W panelu narzędzi znajdź **System Boundary** (prostokąt z nazwą)
2. Kliknij i narysuj duży prostokąt w centrum diagramu
3. Wpisz nazwę: "StayFinder Hotel Booking System"

**RU:**
1. В панели инструментов найдите **System Boundary** (прямоугольник с именем)
2. Щелкните и нарисуйте большой прямоугольник в центре диаграммы
3. Введите имя: "StayFinder Hotel Booking System"

### Krok 6: Dodaj przypadki użycia (Use Cases)
**PL:**
W systemie StayFinder mamy następujące grupy przypadków użycia:

**RU:**
В системе StayFinder у нас следующие группы вариантов использования:

#### 6.1. Funkcje publiczne (Public Features)
**PL:**
Dodaj następujące przypadki użycia (elipsy) wewnątrz granicy systemu:
1. W panelu narzędzi wybierz **Use Case** (elipsa)
2. Kliknij wewnątrz granicy systemu
3. Dodaj następujące przypadki użycia:
   - "Browse Hotels" (Przeglądaj hotele)
   - "Search Hotels" (Szukaj hoteli)
   - "View Hotel Details" (Zobacz szczegóły hotelu)
   - "View Room Information" (Zobacz informacje o pokoju)

**RU:**
Добавьте следующие варианты использования (эллипсы) внутри границы системы:
1. В панели инструментов выберите **Use Case** (эллипс)
2. Щелкните внутри границы системы
3. Добавьте следующие варианты использования:
   - "Browse Hotels" (Просмотр отелей)
   - "Search Hotels" (Поиск отелей)
   - "View Hotel Details" (Просмотр деталей отеля)
   - "View Room Information" (Просмотр информации о номере)

#### 6.2. Uwierzytelnianie (Authentication)
**PL:**
Dodaj przypadki użycia:
- "Register Account" (Zarejestruj konto)
- "Login" (Zaloguj się)
- "Confirm Email" (Potwierdź email)
- "Reset Password" (Zresetuj hasło)
- "Logout" (Wyloguj się)

**RU:**
Добавьте варианты использования:
- "Register Account" (Регистрация аккаунта)
- "Login" (Вход в систему)
- "Confirm Email" (Подтверждение email)
- "Reset Password" (Сброс пароля)
- "Logout" (Выход из системы)

#### 6.3. Zarządzanie rezerwacjami (Booking Management)
**PL:**
Dodaj przypadki użycia:
- "Create Booking" (Utwórz rezerwację)
- "View My Reservations" (Zobacz moje rezerwacje)
- "Cancel Reservation" (Anuluj rezerwację)
- "Check Room Availability" (Sprawdź dostępność pokoju)

**RU:**
Добавьте варианты использования:
- "Create Booking" (Создать бронирование)
- "View My Reservations" (Просмотр моих бронирований)
- "Cancel Reservation" (Отменить бронирование)
- "Check Room Availability" (Проверить доступность номера)

#### 6.4. Przetwarzanie płatności (Payment Processing)
**PL:**
Dodaj przypadki użycia:
- "Initiate Payment" (Rozpocznij płatność)
- "Process Payment" (Przetwórz płatność)
- "Confirm Payment" (Potwierdź płatność)
- "Send Payment Receipt" (Wyślij potwierdzenie płatności)

**RU:**
Добавьте варианты использования:
- "Initiate Payment" (Инициировать платеж)
- "Process Payment" (Обработать платеж)
- "Confirm Payment" (Подтвердить платеж)
- "Send Payment Receipt" (Отправить квитанцию платежа)

#### 6.5. Panel administracyjny (Admin Panel)
**PL:**
Dodaj przypadki użycia:
- "Admin Login" (Logowanie administratora)
- "View Dashboard" (Zobacz panel główny)
- "Manage Hotels" (Zarządzaj hotelami)
- "Manage Rooms" (Zarządzaj pokojami)
- "Manage Reservations" (Zarządzaj rezerwacjami)
- "View Payments" (Zobacz płatności)
- "View Users" (Zobacz użytkowników)
- "Update Reservation Status" (Aktualizuj status rezerwacji)

**RU:**
Добавьте варианты использования:
- "Admin Login" (Вход администратора)
- "View Dashboard" (Просмотр панели управления)
- "Manage Hotels" (Управление отелями)
- "Manage Rooms" (Управление номерами)
- "Manage Reservations" (Управление бронированиями)
- "View Payments" (Просмотр платежей)
- "View Users" (Просмотр пользователей)
- "Update Reservation Status" (Обновить статус бронирования)

### Krok 7: Połącz aktorów z przypadkami użycia
**PL:**
1. W panelu narzędzi wybierz **Association** (linia)
2. Kliknij na aktora, a następnie na przypadek użycia
3. Połącz:

**RU:**
1. В панели инструментов выберите **Association** (линия)
2. Щелкните на актора, затем на вариант использования
3. Соедините:

#### Połączenia Guest:
- Guest → Browse Hotels
- Guest → Search Hotels
- Guest → View Hotel Details
- Guest → View Room Information
- Guest → Register Account

#### Połączenia Registered User:
**PL:**
1. Utwórz **Generalizację** (trójkątna strzałka) od Registered User do Guest
   - W panelu narzędzi wybierz **Generalization**
   - Kliknij Registered User, następnie Guest
2. Połącz Registered User z:
   - Login
   - Confirm Email
   - Reset Password
   - Logout
   - Create Booking
   - View My Reservations
   - Cancel Reservation
   - Initiate Payment

**RU:**
1. Создайте **Generalization** (треугольная стрелка) от Registered User до Guest
   - В панели инструментов выберите **Generalization**
   - Щелкните Registered User, затем Guest
2. Соедините Registered User с:
   - Login
   - Confirm Email
   - Reset Password
   - Logout
   - Create Booking
   - View My Reservations
   - Cancel Reservation
   - Initiate Payment

#### Połączenia Administrator:
**PL:**
Połącz Administrator ze wszystkimi przypadkami użycia Admin Panel

**RU:**
Соедините Administrator со всеми вариантами использования Admin Panel

#### Połączenia Stripe Payment System:
- Stripe → Process Payment
- Stripe → Confirm Payment

### Krok 8: Dodaj relacje między przypadkami użycia
**PL:**
Relacje **<<include>>** (jedna funkcja zawsze wymaga innej):

**RU:**
Связи **<<include>>** (одна функция всегда требует другую):

1. W panelu narzędzi wybierz **Include**
2. Dodaj relacje:
   - Create Booking → Check Room Availability
   - Initiate Payment → Process Payment
   - Confirm Payment → Send Payment Receipt
   - Manage Hotels → Manage Rooms

**PL:**
Relacje **<<extend>>** (jedna funkcja opcjonalnie rozszerza inną):

**RU:**
Связи **<<extend>>** (одна функция опционально расширяет другую):

1. W panelu narzędzi wybierz **Extend**
2. Dodaj relacje:
   - Register Account ← Confirm Email
   - Confirm Payment ← Update Reservation Status

### Krok 9: Dodaj notatki (opcjonalnie)
**PL:**
1. Wybierz **Note** z panelu narzędzi
2. Dodaj notatki dla każdego aktora wyjaśniające ich rolę

**RU:**
1. Выберите **Note** из панели инструментов
2. Добавьте заметки для каждого актора, объясняющие их роль

---

## 💾 Eksport i zapisywanie / Экспорт и сохранение

### Krok 10: Zapisz projekt
**PL:**
1. Kliknij **File → Save Project**
2. Wybierz lokalizację i nazwę pliku
3. Zapisz jako **StayFinder.vpp**

**RU:**
1. Нажмите **File → Save Project**
2. Выберите место и имя файла
3. Сохраните как **StayFinder.vpp**

### Krok 11: Eksportuj diagram jako obraz
**PL:**
1. Kliknij **File → Export → Active Diagram as Image...**
2. Wybierz format (PNG lub JPEG)
3. Ustaw rozdzielczość (zalecane: 300 DPI)
4. Kliknij **OK** i wybierz miejsce zapisu

**RU:**
1. Нажмите **File → Export → Active Diagram as Image...**
2. Выберите формат (PNG или JPEG)
3. Установите разрешение (рекомендуется: 300 DPI)
4. Нажмите **OK** и выберите место сохранения

### Krok 12: Eksportuj do PDF (opcjonalnie)
**PL:**
1. Kliknij **File → Export → Active Diagram as PDF...**
2. Wybierz opcje eksportu
3. Zapisz plik PDF

**RU:**
1. Нажмите **File → Export → Active Diagram as PDF...**
2. Выберите опции экспорта
3. Сохраните файл PDF

---

## 📚 Dodatkowe wskazówki / Дополнительные подсказки

### Formatowanie diagramu / Форматирование диаграммы

**PL:**
- **Wyrównanie:** Używaj **Format → Alignment** aby wyrównać elementy
- **Rozmiar:** Kliknij prawym przyciskiem na element → **Presentation Options** → dostosuj rozmiar
- **Kolory:** Kliknij prawym → **Presentation Options** → **Fill** → wybierz kolor
- **Czcionka:** Kliknij prawym → **Presentation Options** → **Font** → zmień czcionkę

**RU:**
- **Выравнивание:** Используйте **Format → Alignment** для выравнивания элементов
- **Размер:** Щелкните правой кнопкой на элементе → **Presentation Options** → настройте размер
- **Цвета:** Щелкните правой → **Presentation Options** → **Fill** → выберите цвет
- **Шрифт:** Щелкните правой → **Presentation Options** → **Font** → измените шрифт

### Częste problemy / Частые проблемы

**PL:**
**Problem:** Nie mogę połączyć elementów
**Rozwiązanie:** Upewnij się, że wybrałeś odpowiedni typ połączenia z panelu narzędzi

**Problem:** Elementy nachodzą na siebie
**Rozwiązanie:** Użyj **Format → Arrange → Auto Layout** aby automatycznie uporządkować diagram

**Problem:** Diagram jest za mały/duży
**Rozwiązanie:** Użyj narzędzia Zoom (dolny prawy róg) lub klawiszy Ctrl + / Ctrl -

**RU:**
**Проблема:** Не могу соединить элементы
**Решение:** Убедитесь, что выбрали правильный тип соединения из панели инструментов

**Проблема:** Элементы накладываются друг на друга
**Решение:** Используйте **Format → Arrange → Auto Layout** для автоматического упорядочивания диаграммы

**Проблема:** Диаграмма слишком маленькая/большая
**Решение:** Используйте инструмент Zoom (нижний правый угол) или клавиши Ctrl + / Ctrl -

---

## ✅ Sprawdzenie / Проверка

**PL:**
Po zakończeniu upewnij się, że:
- [x] Wszystkie 4 aktorów są na diagramie
- [x] Wszystkie przypadki użycia są wewnątrz granicy systemu
- [x] Połączenia między aktorami a przypadkami użycia są prawidłowe
- [x] Relacje <<include>> i <<extend>> są poprawnie oznaczone
- [x] Diagram jest czytelny i estetyczny
- [x] Projekt został zapisany jako .vpp
- [x] Diagram został wyeksportowany jako obraz

**RU:**
После завершения убедитесь, что:
- [x] Все 4 актора на диаграмме
- [x] Все варианты использования внутри границы системы
- [x] Связи между акторами и вариантами использования правильные
- [x] Отношения <<include>> и <<extend>> правильно обозначены
- [x] Диаграмма читаемая и эстетичная
- [x] Проект сохранен как .vpp
- [x] Диаграмма экспортирована как изображение

---

## 📖 Źródła / Источники

**PL:**
- Visual Paradigm dokumentacja: https://www.visual-paradigm.com/support/
- UML Use Case Diagram tutorial: https://www.visual-paradigm.com/guide/uml-unified-modeling-language/what-is-use-case-diagram/

**RU:**
- Документация Visual Paradigm: https://www.visual-paradigm.com/support/
- Туториал по диаграммам вариантов использования UML: https://www.visual-paradigm.com/guide/uml-unified-modeling-language/what-is-use-case-diagram/

---

## 📧 Potrzebujesz pomocy? / Нужна помощь?

**PL:**
Jeśli masz pytania lub problemy, możesz:
- Sprawdzić oficjalną dokumentację Visual Paradigm
- Obejrzeć tutoriale wideo na YouTube: "Visual Paradigm use case diagram"
- Odwiedzić forum Visual Paradigm

**RU:**
Если у вас есть вопросы или проблемы, вы можете:
- Проверить официальную документацию Visual Paradigm
- Посмотреть видео-туториалы на YouTube: "Visual Paradigm use case diagram"
- Посетить форум Visual Paradigm

---

**Powodzenia! / Удачи!** 🎉
