# Diagram Przypadków Użycia / Use Case Diagram
## StayFinder - Hotel Booking System

---

## 📁 Files / Pliki / Файлы

### Main Files / Główne pliki / Основные файлы

1. **use-case-diagram.puml** - PlantUML source code for the use case diagram
   - Format: PlantUML
   - Can be opened in: PlantUML, Visual Studio Code (with PlantUML extension), online PlantUML editor
   - To import in Visual Paradigm: File → Import → PlantUML File

2. **StayFinder Use Case Diagram.png** - Generated diagram image
   - Format: PNG image
   - Ready to use in presentations and documentation
   - Can be inserted into Visual Paradigm as a reference image

3. **USE-CASE-INSTRUCTIONS.md** - Complete step-by-step instructions
   - In Polish and Russian
   - Detailed guide for creating the diagram in Visual Paradigm from scratch
   - Perfect for beginners ("чайник")

4. **USE-CASE-DESCRIPTION.md** - Detailed description of all use cases
   - In English, Polish, and Russian
   - Complete documentation of all actors, use cases, and relationships
   - Technical implementation details

---

## 🚀 Quick Start / Szybki start / Быстрый старт

### Option 1: Use the provided PlantUML file (Easiest)
**EN:** Import the `use-case-diagram.puml` file into Visual Paradigm.  
**PL:** Zaimportuj plik `use-case-diagram.puml` do Visual Paradigm.  
**RU:** Импортируйте файл `use-case-diagram.puml` в Visual Paradigm.

**Steps:**
1. Open Visual Paradigm
2. File → Import → PlantUML File...
3. Select `use-case-diagram.puml`
4. The diagram will be automatically created

---

### Option 2: Create manually (Learning experience)
**EN:** Follow the detailed instructions in `USE-CASE-INSTRUCTIONS.md`  
**PL:** Postępuj zgodnie ze szczegółową instrukcją w `USE-CASE-INSTRUCTIONS.md`  
**RU:** Следуйте подробной инструкции в `USE-CASE-INSTRUCTIONS.md`

This is recommended if you want to:
- Learn how to use Visual Paradigm
- Understand each component of the diagram
- Customize the diagram to your preferences

---

### Option 3: Use the image as reference
**EN:** Open `StayFinder Use Case Diagram.png` and recreate in Visual Paradigm  
**PL:** Otwórz `StayFinder Use Case Diagram.png` i odtwórz w Visual Paradigm  
**RU:** Откройте `StayFinder Use Case Diagram.png` и воссоздайте в Visual Paradigm

---

## 📊 Diagram Overview / Przegląd diagramu / Обзор диаграммы

### Actors / Aktorzy / Акторы (4)

1. **Guest** (Gość / Гость) - Unregistered visitor
2. **Registered User** (Zarejestrowany użytkownik / Зарегистрированный пользователь) - Logged-in user
3. **Administrator** (Administrator / Администратор) - System admin
4. **Stripe Payment System** (System płatności Stripe / Система платежей Stripe) - External payment service

### Use Case Packages / Pakiety / Пакеты (5)

1. **Public Features** (4 use cases)
   - Browse Hotels
   - Search Hotels
   - View Hotel Details
   - View Room Information

2. **Authentication** (5 use cases)
   - Register Account
   - Login
   - Confirm Email
   - Reset Password
   - Logout

3. **Booking Management** (4 use cases)
   - Create Booking
   - View My Reservations
   - Cancel Reservation
   - Check Room Availability

4. **Payment Processing** (4 use cases)
   - Initiate Payment
   - Process Payment
   - Confirm Payment
   - Send Payment Receipt

5. **Admin Panel** (8 use cases)
   - Admin Login
   - View Dashboard
   - Manage Hotels
   - Manage Rooms
   - Manage Reservations
   - View Payments
   - View Users
   - Update Reservation Status

**Total: 25 use cases**

---

## 🔗 Key Relationships / Kluczowe relacje / Ключевые отношения

### Inheritance / Dziedziczenie / Наследование
- Registered User **inherits from** Guest (has all Guest capabilities + more)

### Include / Zawiera / Включает
- Create Booking → Check Room Availability
- Initiate Payment → Process Payment
- Confirm Payment → Send Payment Receipt
- Manage Hotels → Manage Rooms

### Extend / Rozszerza / Расширяет
- Register Account ← Confirm Email
- Confirm Payment ← Update Reservation Status

---

## 🛠️ Tools / Narzędzia / Инструменты

### Required / Wymagane / Необходимые
- **Visual Paradigm** (Community Edition or Trial)
  - Download: https://www.visual-paradigm.com/download/

### Optional / Opcjonalne / Опциональные
- **PlantUML** - For editing .puml files
- **VS Code with PlantUML extension** - For preview and editing
- **Online PlantUML editor** - https://www.plantuml.com/plantuml/

---

## 📖 Documentation Structure / Struktura dokumentacji / Структура документации

```
docs/
├── README.md                      ← You are here / Jesteś tutaj / Вы здесь
├── use-case-diagram.puml          ← Source code / Kod źródłowy / Исходный код
├── StayFinder Use Case Diagram.png ← Generated image / Wygenerowany obraz / Созданное изображение
├── USE-CASE-INSTRUCTIONS.md       ← Step-by-step guide / Instrukcja krok po kroku / Пошаговая инструкция
└── USE-CASE-DESCRIPTION.md        ← Detailed description / Szczegółowy opis / Подробное описание
```

---

## 💡 Tips for Visual Paradigm / Wskazówki / Подсказки

### Import PlantUML / Importowanie PlantUML / Импорт PlantUML
```
File → Import → PlantUML File...
```

### Export Diagram / Eksport diagramu / Экспорт диаграммы
```
File → Export → Active Diagram as Image...
```

### Auto Layout / Automatyczne układanie / Автоматическая компоновка
```
Format → Arrange → Auto Layout
```

### Save Project / Zapisz projekt / Сохранить проект
```
File → Save Project (Ctrl+S)
Save as: StayFinder.vpp
```

---

## 🎓 Learning Resources / Materiały edukacyjne / Обучающие материалы

### Visual Paradigm Tutorials
- Official docs: https://www.visual-paradigm.com/support/
- Use Case Diagram tutorial: https://www.visual-paradigm.com/guide/uml-unified-modeling-language/what-is-use-case-diagram/
- Video tutorials: Search "Visual Paradigm use case diagram" on YouTube

### UML Resources
- UML Use Case Diagram basics: https://en.wikipedia.org/wiki/Use_case_diagram
- Best practices for use case diagrams

---

## ❓ FAQ / Często zadawane pytania / Часто задаваемые вопросы

### Q: Czy mogę edytować plik .puml? / Can I edit the .puml file?
**A:** Yes! Open it in any text editor. PlantUML uses simple text syntax.

### Q: Как импортировать в Visual Paradigm? / How to import to Visual Paradigm?
**A:** File → Import → PlantUML File → Select `use-case-diagram.puml`

### Q: Do I need to pay for Visual Paradigm?
**A:** No, Community Edition is free for non-commercial use.

### Q: Czy diagram jest kompletny? / Is the diagram complete?
**A:** Yes, it covers all features of the StayFinder system based on the code analysis.

### Q: Могу ли я изменить диаграмму? / Can I modify the diagram?
**A:** Yes! Both the .puml file and imported VP project can be modified.

---

## 📞 Support / Wsparcie / Поддержка

**EN:** For detailed instructions on creating the diagram from scratch, see `USE-CASE-INSTRUCTIONS.md`

**PL:** Aby uzyskać szczegółową instrukcję tworzenia diagramu od podstaw, zobacz `USE-CASE-INSTRUCTIONS.md`

**RU:** Для подробной инструкции по созданию диаграммы с нуля см. `USE-CASE-INSTRUCTIONS.md`

---

## ✅ Checklist / Lista kontrolna / Контрольный список

- [x] PlantUML source file created
- [x] Diagram image generated
- [x] Step-by-step instructions written (PL/RU)
- [x] Detailed use case descriptions (EN/PL/RU)
- [x] All 4 actors identified
- [x] All 25 use cases documented
- [x] All relationships defined
- [x] Ready for import to Visual Paradigm

---

**Created:** 2026-02-01  
**Project:** StayFinder Hotel Booking System  
**Version:** 1.0

**Good luck! / Powodzenia! / Удачи!** 🎉
