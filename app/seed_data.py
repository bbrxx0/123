from app import db
from app.models import Hotel, Room

def seed_poland_hotels():
    # If already seeded (>= 9 hotels), do nothing
    if Hotel.query.count() >= 9:
        return

    # Clear existing data to avoid duplicates
    Room.query.delete()
    Hotel.query.delete()
    db.session.commit()

    hotels = [
        {
            "name": "Raffles Europejski Warsaw",
            "city": "Warsaw",
            "address": "Krakowskie Przedmieście 13, Warsaw",
            "stars": 5,
            "image_url": "/static/img/hotel_01.jpg",
            "description": "Iconic luxury hotel in the heart of Warsaw, blending historic elegance with modern comfort.",
            "highlights": "Prime central location\nFull-service spa & wellness\nButler service\nRefined dining & bar",
            "rooms": [
                ("Deluxe King", 2, 1600, "Elegant room with premium amenities."),
                ("Executive Suite", 3, 2400, "Spacious suite for business or special stays."),
                ("Heritage Suite", 3, 3000, "Signature suite inspired by the hotel's history."),
            ]
        },
        {
            "name": "Hotel Bristol, a Luxury Collection Hotel, Warsaw",
            "city": "Warsaw",
            "address": "Krakowskie Przedmieście 42/44, Warsaw",
            "stars": 5,
            "image_url": "/static/img/hotel_02.jpg",
            "description": "A historic landmark on the Royal Route—classic style, grand interiors, and a top city-center base.",
            "highlights": "Royal Route location\nHistoric landmark since 1901\nSpa & pool access\nArt Nouveau / Art Deco interiors",
            "rooms": [
                ("Superior Queen", 2, 980, "Comfortable room in a classic setting."),
                ("Deluxe Double", 2, 1250, "Upgraded room with refined details."),
                ("Luxury Suite", 3, 1900, "More space, living area, premium comfort."),
            ]
        },
        {
            "name": "H15 Boutique Hotel, Warsaw",
            "city": "Warsaw",
            "address": "Poznańska 15, Warsaw",
            "stars": 5,
            "image_url": "/static/img/hotel_03.jpg",
            "description": "Boutique, design-forward hotel with large apartments and a Michelin-recommended restaurant.",
            "highlights": "Spacious apartments\nKitchenette in many rooms\nSignature Restaurant\nGreat city-center location",
            "rooms": [
                ("Studio Apartment", 2, 760, "Large studio with kitchenette."),
                ("Premium Apartment", 3, 980, "Extra space, seating area, modern design."),
                ("Penthouse Suite", 4, 1600, "Top-level comfort with premium features."),
            ]
        },
        {
            "name": "Hotel Stary",
            "city": "Kraków",
            "address": "Szczepańska 5, Kraków",
            "stars": 5,
            "image_url": "/static/img/hotel_04.jpg",
            "description": "Luxury stay in Kraków Old Town with standout interior design and an on-site spa & pools.",
            "highlights": "Old Town location\nRooftop terrace & seasonal sky bar\nSpa with sauna/steam\nTwo pools (with jets)",
            "rooms": [
                ("Classic Double", 2, 820, "Classic comfort in a historic setting."),
                ("Junior Suite", 3, 1100, "More space, boutique feel."),
                ("Royal Suite", 3, 1750, "Premium suite for special occasions."),
            ]
        },
        {
            "name": "PURO Kraków Kazimierz",
            "city": "Kraków",
            "address": "ul. Halicka 14A, Kraków",
            "stars": 4,
            "image_url": "/static/img/hotel_05.jpg",
            "description": "Modern lifestyle hotel in the vibrant Kazimierz district with spa access and great design.",
            "highlights": "Kazimierz district base\nPrisma Spa & sauna\nFree bike rental (weather permitting)\nFitness & stylish common areas",
            "rooms": [
                ("Standard Double", 2, 520, "Minimalist, modern room."),
                ("Comfort King", 2, 650, "Bigger bed, more comfort."),
                ("Family Room", 4, 860, "Extra space for families."),
            ]
        },
        {
            "name": "Hilton Gdańsk",
            "city": "Gdańsk",
            "address": "Targ Rybny 1, Gdańsk",
            "stars": 5,
            "image_url": "/static/img/hotel_06.jpg",
            "description": "Waterfront Old Town hotel on the Motława River with a spa and rooftop indoor pool views.",
            "highlights": "Motława River waterfront\nOld Town walkable location\nSpa treatments\nTop-floor indoor pool with views",
            "rooms": [
                ("King Guest Room", 2, 780, "Modern room with premium bedding."),
                ("River View Room", 2, 920, "Views toward the river/Old Town."),
                ("Executive Suite", 3, 1400, "Extra space for work & rest."),
            ]
        },
        {
            "name": "Radisson Blu Hotel, Sopot",
            "city": "Sopot",
            "address": "Bitwy pod Płowcami 54, Sopot",
            "stars": 4,
            "image_url": "/static/img/hotel_07.jpg",
            "description": "Beach-friendly stay in Sopot with a major spa zone and a large swimming pool.",
            "highlights": "Near Sopot beach\nSpa with sauna area\nLarge hotel pool\nGreat for couples & families",
            "rooms": [
                ("Standard Double", 2, 620, "Comfortable room for a seaside trip."),
                ("Superior Room", 2, 790, "More space, upgraded amenities."),
                ("Family Suite", 4, 1050, "Family-friendly layout and comfort."),
            ]
        },
        {
            "name": "The Granary - La Suite Hotel",
            "city": "Wrocław",
            "address": "Mennicza 24, Wrocław",
            "stars": 5,
            "image_url": "/static/img/hotel_08.jpg",
            "description": "5-star boutique hotel housed in a historic 16th-century granary in central Wrocław.",
            "highlights": "Historic 16th-century granary building\nCentral Wrocław location\nBoutique suites\nSpa services available",
            "rooms": [
                ("Boutique Double", 2, 680, "Cozy boutique room with character."),
                ("Loft Suite", 3, 980, "Suite inspired by the building's geometry."),
                ("Premium Suite", 4, 1350, "Spacious suite for longer stays."),
            ]
        },
        {
            "name": "Nosalowy Park Hotel & Spa",
            "city": "Zakopane",
            "address": "Kościuszki 18, Zakopane",
            "stars": 5,
            "image_url": "/static/img/hotel_09.jpg",
            "description": "5-star spa hotel in central Zakopane, a short walk to Krupówki and close to mountain attractions.",
            "highlights": "Central Zakopane (near Krupówki)\nNABE Spa & wellness zone\nPool + outdoor jacuzzi\nSaunas & brine graduation tower",
            "rooms": [
                ("Classic Double", 2, 740, "Comfortable base for mountain trips."),
                ("Deluxe Room", 2, 940, "Upgraded comfort with premium finish."),
                ("Suite with Balcony", 4, 1350, "More space and balcony for views."),
            ]
        },
    ]

    for h in hotels:
        hotel = Hotel(
            name=h["name"],
            city=h["city"],
            address=h["address"],
            stars=h["stars"],
            image_url=h["image_url"],
            description=h["description"],
            highlights=h["highlights"],
        )
        db.session.add(hotel)
        db.session.flush()

        for (rname, cap, price, rdesc) in h["rooms"]:
            db.session.add(Room(
                hotel_id=hotel.id,
                name=rname,
                capacity=cap,
                price_per_night=price,
                description=rdesc
            ))

    db.session.commit()
