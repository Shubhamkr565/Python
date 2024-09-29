travel_log = [
    {
    "country": "India",
    "cityes_visited": ["Delhi", "Mumbai", "Goa", "Rajasthan", "Jaipur","Bengaluru", "Jammu&Kashmir"],
    "total_visits": 7,
    },
    {
        "country": "France",
        "cityes_visited": ["Paris", "Lyon", "Nantes", "Lille", "Dijon"],
        "total_visits": 5,
    }
]


def add_new_country(country_visited, total_visited, city_visited):
    new_country  = {}
    new_country["country"] = country_visited
    new_country["total_visit"] = total_visited
    new_country["city"] = city_visited
    travel_log.append(new_country)


add_new_country("Russia", 2, ["Moscow", "Saint petersbu"], )
print(travel_log)