# StayFinder - Use Case Diagram Description
## Opis diagramu przypadków użycia / Описание диаграммы вариантов использования

---

## 📊 System Overview / Przegląd systemu / Обзор системы

**EN:** StayFinder is a hotel booking system that allows guests to search and book hotel rooms, make payments, and manage their reservations.

**PL:** StayFinder to system rezerwacji hoteli, który umożliwia gościom wyszukiwanie i rezerwowanie pokoi hotelowych, dokonywanie płatności oraz zarządzanie rezerwacjami.

**RU:** StayFinder - это система бронирования отелей, которая позволяет гостям искать и бронировать номера в отелях, совершать платежи и управлять своими бронированиями.

---

## 👥 Actors / Aktorzy / Акторы

### 1. Guest (Gość / Гость)
**EN:** An unregistered user who can browse hotels and register for an account.

**PL:** Niezarejestrowany użytkownik, który może przeglądać hotele i rejestrować się w systemie.

**RU:** Незарегистрированный пользователь, который может просматривать отели и зарегистрироваться в системе.

**Capabilities / Możliwości / Возможности:**
- Browse hotels (Przeglądanie hoteli / Просмотр отелей)
- Search hotels by name or city (Wyszukiwanie hoteli po nazwie lub mieście / Поиск отелей по названию или городу)
- View hotel details (Przeglądanie szczegółów hoteli / Просмотр деталей отелей)
- View room information (Przeglądanie informacji o pokojach / Просмотр информации о номерах)
- Register account (Rejestracja konta / Регистрация аккаунта)

---

### 2. Registered User (Zarejestrowany użytkownik / Зарегистрированный пользователь)
**EN:** A user who has created an account and can make bookings.

**PL:** Użytkownik, który utworzył konto i może dokonywać rezerwacji.

**RU:** Пользователь, который создал аккаунт и может делать бронирования.

**Inherits from / Dziedziczy po / Наследует от:** Guest

**Additional Capabilities / Dodatkowe możliwości / Дополнительные возможности:**
- Login/Logout (Logowanie/Wylogowanie / Вход/Выход)
- Confirm email (Potwierdzenie emaila / Подтверждение email)
- Reset password (Resetowanie hasła / Сброс пароля)
- Create booking (Tworzenie rezerwacji / Создание бронирования)
- View personal reservations (Przeglądanie własnych rezerwacji / Просмотр личных бронирований)
- Cancel reservation (Anulowanie rezerwacji / Отмена бронирования)
- Initiate payment (Rozpoczęcie płatności / Инициирование платежа)

---

### 3. Administrator (Administrator / Администратор)
**EN:** System administrator who manages hotels, rooms, users, and reservations.

**PL:** Administrator systemu, który zarządza hotelami, pokojami, użytkownikami i rezerwacjami.

**RU:** Администратор системы, который управляет отелями, номерами, пользователями и бронированиями.

**Capabilities / Możliwości / Возможности:**
- Admin login (Logowanie administratora / Вход администратора)
- View dashboard with statistics (Przeglądanie panelu ze statystykami / Просмотр панели со статистикой)
- Manage hotels (CRUD operations) (Zarządzanie hotelami / Управление отелями)
- Manage rooms (CRUD operations) (Zarządzanie pokojami / Управление номерами)
- Manage reservations (Zarządzanie rezerwacjami / Управление бронированиями)
- View all payments (Przeglądanie wszystkich płatności / Просмотр всех платежей)
- View all users (Przeglądanie wszystkich użytkowników / Просмотр всех пользователей)
- Update reservation status (Aktualizacja statusu rezerwacji / Обновление статуса бронирования)

---

### 4. Stripe Payment System (System płatności Stripe / Система платежей Stripe)
**EN:** External payment processing system that handles transactions.

**PL:** Zewnętrzny system przetwarzania płatności, który obsługuje transakcje.

**RU:** Внешняя система обработки платежей, которая обрабатывает транзакции.

**Capabilities / Możliwości / Возможности:**
- Process payment (Przetwarzanie płatności / Обработка платежа)
- Confirm payment (Potwierdzanie płatności / Подтверждение платежа)

---

## 📦 Use Case Packages / Pakiety przypadków użycia / Пакеты вариантов использования

### Package 1: Public Features (Funkcje publiczne / Публичные функции)

#### UC1: Browse Hotels
**EN:** Guest can view a list of all available hotels.
**PL:** Gość może przeglądać listę wszystkich dostępnych hoteli.
**RU:** Гость может просматривать список всех доступных отелей.

**Actors:** Guest (and all inherited)
**Preconditions:** None
**Flow:**
1. User navigates to homepage
2. System displays list of hotels
3. Hotels are shown with basic information (name, city, stars, image)

---

#### UC2: Search Hotels
**EN:** Guest can search for hotels by name or city.
**PL:** Gość może wyszukiwać hotele po nazwie lub mieście.
**RU:** Гость может искать отели по названию или городу.

**Actors:** Guest (and all inherited)
**Preconditions:** None
**Flow:**
1. User enters search criteria (name or city)
2. System filters hotels based on criteria
3. System displays matching results

---

#### UC3: View Hotel Details
**EN:** Guest can view detailed information about a specific hotel.
**PL:** Gość może przeglądać szczegółowe informacje o konkretnym hotelu.
**RU:** Гость может просматривать подробную информацию о конкретном отеле.

**Actors:** Guest (and all inherited)
**Preconditions:** Hotel exists in system
**Flow:**
1. User clicks on a hotel
2. System displays hotel details (name, city, address, description, highlights, stars)
3. System shows available rooms for this hotel

---

#### UC4: View Room Information
**EN:** Guest can view details about a specific room.
**PL:** Gość może przeglądać szczegóły dotyczące konkretnego pokoju.
**RU:** Гость может просматривать детали о конкретном номере.

**Actors:** Guest (and all inherited)
**Preconditions:** Room exists in system
**Flow:**
1. User views hotel details
2. User clicks on a room
3. System displays room information (name, capacity, price per night, description)

---

### Package 2: Authentication (Uwierzytelnianie / Аутентификация)

#### UC5: Register Account
**EN:** Guest can create a new user account.
**PL:** Gość może utworzyć nowe konto użytkownika.
**RU:** Гость может создать новый аккаунт пользователя.

**Actors:** Guest
**Preconditions:** Email not already registered
**Flow:**
1. Guest navigates to registration page
2. Guest enters email and password
3. System creates account with unconfirmed email status
4. System sends confirmation email
5. **<<extend>>** Confirm Email (UC7)

**Postconditions:** Account created but not yet confirmed

---

#### UC6: Login
**EN:** Registered user can log into the system.
**PL:** Zarejestrowany użytkownik może zalogować się do systemu.
**RU:** Зарегистрированный пользователь может войти в систему.

**Actors:** Registered User
**Preconditions:** Account exists and email is confirmed (for non-admin users)
**Flow:**
1. User navigates to login page
2. User enters email and password
3. System validates credentials
4. If valid and email confirmed, user is logged in
5. User is redirected to homepage or requested page

**Alternative Flow:**
- If email not confirmed: System shows message to confirm email first
- If credentials invalid: System shows error message

---

#### UC7: Confirm Email
**EN:** User confirms their email address via a link sent to their email.
**PL:** Użytkownik potwierdza swój adres email poprzez link wysłany na email.
**RU:** Пользователь подтверждает свой адрес email через ссылку, отправленную на email.

**Actors:** Registered User
**Preconditions:** Account created, confirmation token valid
**Flow:**
1. User receives email with confirmation link
2. User clicks on confirmation link
3. System validates token
4. System marks email as confirmed
5. User can now log in

---

#### UC8: Reset Password
**EN:** User can reset their password if forgotten.
**PL:** Użytkownik może zresetować hasło w przypadku zapomnienia.
**RU:** Пользователь может сбросить пароль, если забыл.

**Actors:** Registered User
**Preconditions:** Account exists
**Flow:**
1. User navigates to password reset page
2. User enters email address
3. System sends password reset link to email
4. User clicks on reset link
5. User enters new password
6. System updates password
7. User can log in with new password

---

#### UC9: Logout
**EN:** Logged-in user can log out of the system.
**PL:** Zalogowany użytkownik może się wylogować z systemu.
**RU:** Вошедший пользователь может выйти из системы.

**Actors:** Registered User
**Preconditions:** User is logged in
**Flow:**
1. User clicks logout
2. System ends user session
3. User is redirected to homepage

---

### Package 3: Booking Management (Zarządzanie rezerwacjami / Управление бронированиями)

#### UC10: Create Booking
**EN:** Registered user can create a new room booking.
**PL:** Zarejestrowany użytkownik może utworzyć nową rezerwację pokoju.
**RU:** Зарегистрированный пользователь может создать новое бронирование номера.

**Actors:** Registered User
**Preconditions:** User is logged in, room exists
**Flow:**
1. User views room details
2. User clicks "Book" button
3. User selects check-in and check-out dates
4. **<<include>>** Check Room Availability (UC13)
5. If available, system creates booking with "pending" status
6. User is redirected to their reservations page

**Alternative Flow:**
- If room not available: System shows error message and does not create booking

---

#### UC11: View My Reservations
**EN:** Registered user can view all their bookings.
**PL:** Zarejestrowany użytkownik może przeglądać wszystkie swoje rezerwacje.
**RU:** Зарегистрированный пользователь может просматривать все свои бронирования.

**Actors:** Registered User
**Preconditions:** User is logged in
**Flow:**
1. User navigates to "My Reservations" page
2. System retrieves all reservations for the user
3. System displays reservations with details (hotel, room, dates, status, payment status)

---

#### UC12: Cancel Reservation
**EN:** User can cancel an existing reservation.
**PL:** Użytkownik może anulować istniejącą rezerwację.
**RU:** Пользователь может отменить существующее бронирование.

**Actors:** Registered User, Administrator
**Preconditions:** Reservation exists and belongs to user (or user is admin)
**Flow:**
1. User views their reservations
2. User clicks "Cancel" on a reservation
3. System changes reservation status to "canceled"
4. User sees confirmation message

---

#### UC13: Check Room Availability
**EN:** System checks if a room is available for the requested dates.
**PL:** System sprawdza, czy pokój jest dostępny w żądanych terminach.
**RU:** Система проверяет, доступен ли номер на запрашиваемые даты.

**Actors:** System (internal)
**Preconditions:** Room exists, dates are valid
**Flow:**
1. System queries database for overlapping reservations
2. System excludes canceled reservations
3. System checks if any active reservation conflicts with requested dates
4. System returns availability status

**Note:** This is an internal use case included by Create Booking

---

### Package 4: Payment Processing (Przetwarzanie płatności / Обработка платежей)

#### UC14: Initiate Payment
**EN:** User starts the payment process for a booking.
**PL:** Użytkownik rozpoczyna proces płatności za rezerwację.
**RU:** Пользователь начинает процесс оплаты бронирования.

**Actors:** Registered User
**Preconditions:** User is logged in, reservation exists and is not canceled, not already paid
**Flow:**
1. User views their reservations
2. User clicks "Pay" on an unpaid reservation
3. System calculates total price (nights × price per night)
4. **<<include>>** Process Payment (UC15)
5. System creates Stripe checkout session
6. User is redirected to Stripe payment page

---

#### UC15: Process Payment
**EN:** Stripe processes the payment transaction.
**PL:** Stripe przetwarza transakcję płatności.
**RU:** Stripe обрабатывает транзакцию платежа.

**Actors:** Stripe Payment System
**Preconditions:** Checkout session created
**Flow:**
1. User enters payment details on Stripe page
2. Stripe validates card information
3. Stripe processes payment
4. Stripe updates payment status

**Alternative Flow:**
- If payment fails: Stripe notifies system, payment status set to "failed"
- If payment succeeds: Continue to Confirm Payment (UC16)

---

#### UC16: Confirm Payment
**EN:** System confirms successful payment and updates reservation.
**PL:** System potwierdza udaną płatność i aktualizuje rezerwację.
**RU:** Система подтверждает успешный платеж и обновляет бронирование.

**Actors:** Stripe Payment System
**Preconditions:** Payment processed successfully
**Flow:**
1. Stripe redirects user back to application
2. System retrieves payment session from Stripe
3. System marks reservation as "paid"
4. System changes reservation status to "confirmed"
5. **<<include>>** Send Payment Receipt (UC17)
6. **<<extend>>** Update Reservation Status (UC25) - if needed
7. System shows success message to user

---

#### UC17: Send Payment Receipt
**EN:** System sends payment confirmation email to user.
**PL:** System wysyła email z potwierdzeniem płatności do użytkownika.
**RU:** Система отправляет email с подтверждением платежа пользователю.

**Actors:** System (internal)
**Preconditions:** Payment confirmed
**Flow:**
1. System prepares receipt email with booking details
2. System sends email to user's address
3. Email contains payment reference and booking information

---

### Package 5: Admin Panel (Panel administracyjny / Панель администратора)

#### UC18: Admin Login
**EN:** Administrator logs into the admin panel.
**PL:** Administrator loguje się do panelu administracyjnego.
**RU:** Администратор входит в административную панель.

**Actors:** Administrator
**Preconditions:** Account exists and has admin privileges
**Flow:**
1. Admin navigates to /admin/login
2. Admin enters credentials
3. System validates admin credentials
4. If valid, admin is logged in to admin panel
5. Admin is redirected to dashboard

**Alternative Flow:**
- If not admin or invalid credentials: System shows error and logs attempt

---

#### UC19: View Dashboard
**EN:** Administrator views system statistics and overview.
**PL:** Administrator przegląda statystyki systemu i przegląd.
**RU:** Администратор просматривает статистику системы и обзор.

**Actors:** Administrator
**Preconditions:** Admin is logged in
**Flow:**
1. Admin accesses dashboard
2. System displays statistics:
   - Total hotels, rooms, users, reservations
   - Pending, confirmed, canceled reservations
   - Payment statistics (paid, unpaid, failed)
   - Total revenue from paid reservations
   - Upcoming check-ins (next 7 days)
   - Latest reservations, users, and payments

---

#### UC20: Manage Hotels
**EN:** Administrator can create, edit, and delete hotels.
**PL:** Administrator może tworzyć, edytować i usuwać hotele.
**RU:** Администратор может создавать, редактировать и удалять отели.

**Actors:** Administrator
**Preconditions:** Admin is logged in
**Flow:**
- **Create Hotel:**
  1. Admin clicks "New Hotel"
  2. Admin enters hotel details (name, city, address, stars, image URL, highlights, description)
  3. System creates hotel
  4. **<<include>>** Manage Rooms (UC21) - can then add rooms

- **Edit Hotel:**
  1. Admin clicks "Edit" on a hotel
  2. Admin modifies hotel details
  3. System updates hotel

- **Delete Hotel:**
  1. Admin clicks "Delete" on a hotel
  2. System deletes hotel and all associated rooms and reservations (cascade)
  3. System logs the action

---

#### UC21: Manage Rooms
**EN:** Administrator can create, edit, and delete rooms for hotels.
**PL:** Administrator może tworzyć, edytować i usuwać pokoje dla hoteli.
**RU:** Администратор может создавать, редактировать и удалять номера для отелей.

**Actors:** Administrator
**Preconditions:** Admin is logged in, hotel exists
**Flow:**
- **Create Room:**
  1. Admin selects a hotel
  2. Admin clicks "New Room"
  3. Admin enters room details (name, capacity, price per night, description)
  4. System creates room for the hotel

- **Edit Room:**
  1. Admin clicks "Edit" on a room
  2. Admin modifies room details
  3. System updates room

- **Delete Room:**
  1. Admin clicks "Delete" on a room
  2. System deletes room and all associated reservations (cascade)
  3. System logs the action

---

#### UC22: Manage Reservations
**EN:** Administrator can view and filter all reservations.
**PL:** Administrator może przeglądać i filtrować wszystkie rezerwacje.
**RU:** Администратор может просматривать и фильтровать все бронирования.

**Actors:** Administrator
**Preconditions:** Admin is logged in
**Flow:**
1. Admin navigates to reservations list
2. Admin can filter by status (pending, confirmed, canceled)
3. Admin can search by user email, hotel name, or city
4. System displays matching reservations (max 500)
5. Admin can click on reservation to view details

---

#### UC23: View Payments
**EN:** Administrator can view all payment transactions.
**PL:** Administrator może przeglądać wszystkie transakcje płatności.
**RU:** Администратор может просматривать все транзакции платежей.

**Actors:** Administrator
**Preconditions:** Admin is logged in
**Flow:**
1. Admin navigates to payments list
2. Admin can filter by payment status (paid, unpaid, failed)
3. Admin can search by user email, hotel name, or city
4. System displays matching payment records
5. System shows total revenue from displayed paid reservations

---

#### UC24: View Users
**EN:** Administrator can view all registered users.
**PL:** Administrator może przeglądać wszystkich zarejestrowanych użytkowników.
**RU:** Администратор может просматривать всех зарегистрированных пользователей.

**Actors:** Administrator
**Preconditions:** Admin is logged in
**Flow:**
1. Admin navigates to users list
2. System displays all users with details:
   - Email
   - Admin status
   - Email confirmation status
   - Creation date
3. System shows up to 500 users

---

#### UC25: Update Reservation Status
**EN:** Administrator can manually change reservation status.
**PL:** Administrator może ręcznie zmienić status rezerwacji.
**RU:** Администратор может вручную изменить статус бронирования.

**Actors:** Administrator
**Preconditions:** Admin is logged in, reservation exists
**Flow:**
1. Admin views reservation details
2. Admin selects new status (pending, confirmed, canceled)
3. System updates reservation status
4. System logs the status change with admin email
5. System shows confirmation message

---

## 🔗 Relationships / Relacje / Отношения

### Generalization (Dziedziczenie / Обобщение)
- **Registered User** inherits all capabilities from **Guest**

### Include (Zawiera / Включает)
**EN:** One use case always requires another use case.
**PL:** Jeden przypadek użycia zawsze wymaga innego przypadku użycia.
**RU:** Один вариант использования всегда требует другой вариант использования.

- Create Booking **includes** Check Room Availability
- Initiate Payment **includes** Process Payment
- Confirm Payment **includes** Send Payment Receipt
- Manage Hotels **includes** Manage Rooms (can manage rooms after creating hotel)

### Extend (Rozszerza / Расширяет)
**EN:** One use case optionally extends another use case.
**PL:** Jeden przypadek użycia opcjonalnie rozszerza inny przypadek użycia.
**RU:** Один вариант использования опционально расширяет другой вариант использования.

- Confirm Email **extends** Register Account (happens after registration)
- Update Reservation Status **extends** Confirm Payment (admin may need to manually confirm)

---

## 💾 Technical Implementation / Implementacja techniczna / Техническая реализация

**Technology Stack:**
- **Backend:** Python Flask
- **Database:** SQLite (SQLAlchemy ORM)
- **Authentication:** Flask-Login
- **Payment:** Stripe API
- **Email:** Gmail SMTP
- **Security:** Token-based email confirmation and password reset

**Database Models:**
- User (id, email, password_hash, is_admin, is_email_confirmed, email_confirmed_at, created_at)
- Hotel (id, name, city, address, description, highlights, stars, image_url, created_at)
- Room (id, hotel_id, name, capacity, price_per_night, description)
- Reservation (id, user_id, room_id, check_in, check_out, status, payment_status, stripe_session_id, stripe_payment_intent_id, paid_at, created_at)

---

## 📝 Notes / Notatki / Заметки

**EN:**
- Email confirmation is optional for admin accounts but required for regular users
- Room availability checking prevents double bookings
- Cascade deletion: Deleting a hotel also deletes all its rooms and reservations
- Cascade deletion: Deleting a room also deletes all its reservations
- Admin actions are logged for audit purposes
- Payment processing is handled securely through Stripe
- Reservation status flow: pending → confirmed (after payment) or canceled
- Payment status flow: unpaid → paid or failed

**PL:**
- Potwierdzenie emaila jest opcjonalne dla kont administratora, ale wymagane dla zwykłych użytkowników
- Sprawdzanie dostępności pokoju zapobiega podwójnym rezerwacjom
- Kaskadowe usuwanie: Usunięcie hotelu usuwa również wszystkie jego pokoje i rezerwacje
- Kaskadowe usuwanie: Usunięcie pokoju usuwa również wszystkie jego rezerwacje
- Akcje administratora są logowane do celów audytu
- Przetwarzanie płatności jest obsługiwane bezpiecznie przez Stripe
- Przepływ statusu rezerwacji: oczekująca → potwierdzona (po płatności) lub anulowana
- Przepływ statusu płatności: nieopłacona → opłacona lub nieudana

**RU:**
- Подтверждение email необязательно для аккаунтов администратора, но обязательно для обычных пользователей
- Проверка доступности номера предотвращает двойные бронирования
- Каскадное удаление: Удаление отеля также удаляет все его номера и бронирования
- Каскадное удаление: Удаление номера также удаляет все его бронирования
- Действия администратора логируются для целей аудита
- Обработка платежей осуществляется безопасно через Stripe
- Поток статуса бронирования: ожидание → подтверждено (после оплаты) или отменено
- Поток статуса платежа: неоплачено → оплачено или не удалось

---

**Document Version:** 1.0  
**Date:** 2026-02-01  
**Project:** StayFinder Hotel Booking System
