Task 0:

Project name: YG Music Vault

Description:

YG Music Vault is a Django-based website that provides information about artists from the popular South Korean music company, YG Entertainment. Our website offers an easy-to-use platform for fans to discover new music, learn about their favorite YG artists, and keep up-to-date with their latest news and releases. With a user-friendly interface and a comprehensive database of YG artists, YG Music Vault is the go-to destination for anyone interested in the vibrant world of K-Pop music.

ER Diagram description(the image is in the repos):

Category has a one-to-many relationship with People, which means that each category can have multiple people, but each person can only belong to one category.

People has a many-to-one relationship with Category, which means that each person belongs to one category, but each category can have multiple people. People also has a many-to-one relationship with User, which represents the user who created the People object.

Audition is a separate entity with its own attributes, and is not related to Category or People.

To access admin panel:

adina

adina123456
