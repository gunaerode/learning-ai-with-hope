class SubfieldsInAI:
    @staticmethod
    def subfields(subfields_list):
        print("Sub-fields in AI are:")
        for field in subfields_list:
            print(field)


class OddEven:
    @staticmethod
    def check(number):
        if number % 2 == 0:
            print(f"{number} is Even number")
        else:
            print(f"{number} is Odd number")


class EligibilityForMarriage:
    @staticmethod
    def eligible(gender, age):
        gender = gender.lower()
        is_eligible = (
            (gender == "male" and age >= 21) or
            (gender == "female" and age >= 18)
        )

        if is_eligible:
            print("ELIGIBLE")
        else:
            print("NOT ELIGIBLE")


class FindPercent:
    @staticmethod
    def percentage(subjects):
        total = sum(subjects.values())
        percentage = (total / (len(subjects) * 100)) * 100

        for subject, marks in subjects.items():
            print(f"{subject}= {marks}")

        print(f"Total : {total}")
        print(f"Percentage : {percentage}")


class Triangle:
    @staticmethod
    def area(height, breadth):
        print(f"Height:{height}")
        print(f"Breadth:{breadth}")
        print("Area formula: (Height*Breadth)/2")
        area = (height * breadth) / 2
        print(f"Area of Triangle: {area}")

    @staticmethod
    def perimeter(height1, height2, breadth):
        print(f"Height1:{height1}")
        print(f"Height2:{height2}")
        print(f"Breadth:{breadth}")
        print("Perimeter formula: Height1+Height2+Breadth")
        perimeter = height1 + height2 + breadth
        print(f"Perimeter of Triangle: {perimeter}")
