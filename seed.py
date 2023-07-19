from app import app
from models import db, Pet, User, Meetup

# Create application context
# with app.app_context():
# Info on application context: https://flask.palletsprojects.com/en/1.1.x/appcontext/
if __name__ == "__main__":
    with app.app_context():
        User.query.delete()
        Pet.query.delete()
        Meetup.query.delete()

        user = User(
            username = "JessicaLee",
            email = "jessicalee@gmail.com",
            profile_pic = "https://i.pinimg.com/236x/ce/d8/4a/ced84a67302c60bd1abaaf9314064433.jpg",
        )

        user.password_hash = "123"

        db.session.add(user)

        user = User(
                username = "SteveLawrence",
                email = "stevelawrence@gmail.com",
                profile_pic = "https://m.media-amazon.com/images/M/MV5BZjVkYjllNGYtMDYwMi00MjhhLTk1MjMtZGM3OTcxMGNmNzlkXkEyXkFqcGdeQXVyMjQwMDg0Ng@@._V1_.jpg"
            )
        
        user.password_hash = "123"

        db.session.add(user)

        user = User(
                username = "BrandiWright",
                email = "brandiwright@gmail.com",
                profile_pic = "https://kristinepaulsenphotography.com/images/Headshots_005.jpg"
            )
        
        user.password_hash = "123"

        db.session.add(user)

        user = User(
                username = "RobHoward",
                email = "robhoward@gmail.com",
                profile_pic = "https://static1.squarespace.com/static/5aa5d49e297114f4397667c5/t/61bcf1718eb2f01b1954b53f/1639772530153/Bo+Chen.jpg"
            )
        
        user.password_hash = "123"

        db.session.add(user)

        user = User(
                username = "AshleyJimenez",
                _password_hash = "123",
                email = "ashleyjimenez@gmail.com",
                profile_pic = "https://random42.com/wp-content/uploads/2019/11/Random42_Shobitha_Logendran-1.jpg"
            )
        
        user.password_hash = "123"

        db.session.add(user)

        pets = [
            Pet(
            user_id=1,
            name="Ben",
            birth_year="2020",
            species="dog",
            breed="Husky",
            profile_pic="https://images.wagwalkingweb.com/media/daily_wag/blog_articles/hero/1685787498.877709/fun-facts-about-siberian-huskies-1.png",
            city="Chantilly",
            state="Virginia",
            country="United States",
            availability="Weekends",
            ),
            Pet(
            user_id=2,
            name="Sparky",
            birth_year="2016",
            species="dog",
            breed="Golden Retriever",
            profile_pic="https://www.dailydogtag.com/wp-content/uploads/2018/06/Alice-G-Patterson-Photography-life-of-a-boat-dog-0050.jpg",
            city="Dayton",
            state="Ohio",
            country="United States",
            availability="Mondays at 6pm",
            ),
            Pet(
            user_id=3,
            name="Coconut",
            birth_year="2022",
            species="dog",
            breed="Maltipoo",
            profile_pic="https://petlandbradenton.com/wp-content/uploads/2023/03/2383872_800-600x450.jpg",
            city="Austin",
            state="Texas",
            country="United States",
            availability="Everyday at 12pm",
            ),
            Pet(
            user_id=4,
            name="Mitsy",
            birth_year="2018",
            species="cat",
            breed="Maine Coon",
            profile_pic="https://image.petmd.com/files/styles/863x625/public/2023-04/Maine-coon-cat.jpg",
            city="Portland",
            state="Maine",
            country="United States",
            availability="Saturday and Sunday from 3-7pm",
            ),
            Pet(
            user_id=5,
            name="Toothless",
            birth_year="2021",
            species="cat",
            breed="Siamese",
            profile_pic="https://www.dutch.com/cdn/shop/articles/shutterstock_1727177056.jpg?v=1678295146",
            city="Orlando",
            state="Florida",
            country="United States",
            availability="Weekdays after 5:30pm",
            ),
        ]

        db.session.add_all(pets)

        meetups = [
            Meetup(
                user_id=1,
                pet_id=1,
                title="Coffee at the dog park",
                details="Calling all dog lovers in Chantilly, Virginia! Join us for a fun-filled morning at the park where we'll be hosting a special meetup for both dogs and their humans. Coffee will be provided, but you're welcome to bring your own snacks and beverages.",
                venue="Dulles Gateway Dog Park",
                street_address="4508 Upper Cub Run Rd",
                city="Chantilly",
                state="Virginia",
                country="United States",
                date="07/21/2023",
                time="2pm",
                image="https://thedogvine.com/wp-content/uploads/2015/03/North-London-Dog-Meetup.jpeg",
            ),
            Meetup(
                user_id=2,
                pet_id=2,
                title="Hike with your pups",
                details="Are you a nature enthusiast with a furry companion who loves to explore the great outdoors? If so, join us for an exciting hiking adventure with our four-legged friends!",
                venue="Eastwood MetroPark",
                street_address="1385 Harshman Rd",
                city="Dayton",
                state="Ohio",
                country="United States",
                date="07/22/2023",
                time="10am",
                image="https://media1.fdncms.com/styleweekly/imager/u/mobilestory/8970389/canine_adv2_ash.jpg",
            ),
            Meetup(
                user_id=3,
                pet_id=3,
                title="Relax at the springs",
                details="Summer got you panting like a dog? Bring your dogs and join us to take a dip in the cool springs!",
                venue="Barkin' Springs",
                street_address="2101 Barton Springs Rd, Austin, TX 78704",
                city="Austin",
                state="Texas",
                country="United States",
                date="07/23/2023",
                time="1pm",
                image="https://img.atlasobscura.com/RoNp9pPGu7xVvK2uk6L9O_fU5K6M748T2Wx54NVnSSM/rt:fit/h:390/q:81/sm:1/scp:1/ar:1/aHR0cHM6Ly9hdGxh/cy1kZXYuczMuYW1h/em9uYXdzLmNvbS91/cGxvYWRzL3BsYWNl/X2ltYWdlcy9iOWU1/MzhmYTRjN2I3Y2M0/OTdfYXVzdGluLXRl/eGFzLTIwMDB4MjAw/MC0yMTY4ZWIzNGEw/NjExNjAyNmZjZGRh/NzE5NWEwYzg5ZWNl/MGZhYjk5LmpwZw.jpg",
            ),
            Meetup(
                user_id=4,
                pet_id=4,
                title="Cat party at the park",
                details="We're throwing our cat a birthday party and you're all invited! Feline-friendly cake will be served.",
                venue="Fort Allen Park",
                street_address="49 Eastern Promenade",
                city="Portland",
                state="Maine",
                country="United States",
                date="07/24/2023",
                time="5pm",
                image="https://lh3.googleusercontent.com/p/AF1QipO5HZZ6Q4iZGuNjZ8eGTxATSv-8Z_6qXPIyucoa=s1360-w1360-h1020",
            ),
            Meetup(
                user_id=5,
                pet_id=5,
                title="Let's walk our cats together",
                details="Does your cat like to take longs walks around the park? If yes, join us for a stroll!",
                venue="Dickson Azalea Park",
                street_address="100 Rosearden Dr",
                city="Orlando",
                state="Florida",
                country="United States",
                date="07/25/2023",
                time="8pm",
                image="https://i.imgur.com/yCmb2yI.jpg",
            )
        ]

        db.session.add_all(meetups)

        db.session.commit()
