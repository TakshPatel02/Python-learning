# your're building a ticket info system for a railway app. basked on seat type , show its features.
# task:
# input: sleeper , ac , general , luxury
# match using match-case
# unknown -> show invalid seat type

seat_type = input("Enter your seat type (sleeper/ac/general/luxury) : ").lower()

match seat_type:
    case "sleeper":
        print("sleeper : non-ac , 3-tier , affordable")
    case "ac":
        print("ac : ac , 3-tier , comfortable")
    case "general":
        print("general : non-ac , bench seating , affordable")
    case "luxury":
        print("luxury : ac , 2-tier , premium")
    case _:
        print("invalid seat type , enter valid seat type from given options.")
        
            