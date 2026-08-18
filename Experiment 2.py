def format_section(style):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)

            if style == "uppercase":
                return result.upper()
            elif style == "border":
                return "=" * 40 + "\n" + result + "\n" + "=" * 40
            elif style == "title":
                return "\n*** " + result.upper() + " ***\n"
            else:
                return result

        return wrapper
    return decorator


class Report:
    report_count = 0

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.sections = []
        Report.report_count += 1

    @classmethod
    def total_reports(cls):
        return cls.report_count

    def add_section(self, heading, content):
        self.sections.append((heading, content))

    @format_section("title")
    def get_title(self):
        return self.title

    def generate(self, style="normal"):
        report = self.get_title()
        report += f"Author: {self.author}\n\n"

        for heading, content in self.sections:
            if style == "uppercase":
                heading = heading.upper()
                content = content.upper()

            elif style == "border":
                heading = f"--- {heading} ---"

            report += f"{heading}\n{content}\n\n"

        return report

    def __str__(self):
        return self.generate()

    def __len__(self):
        return len(self.sections)


print("===== Dynamic Report Generator =====")

title = input("Enter report title: ")
author = input("Enter author name: ")

report = Report(title, author)

while True:
    print("\n1. Add Section")
    print("2. Generate Normal Report")
    print("3. Generate Uppercase Report")
    print("4. Generate Bordered Report")
    print("5. Show Number of Sections")
    print("6. Show Total Reports")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        heading = input("Enter section heading: ")
        content = input("Enter section content: ")
        report.add_section(heading, content)
        print("Section added successfully.")

    elif choice == "2":
        print("\n" + report.generate("normal"))

    elif choice == "3":
        print("\n" + report.generate("uppercase"))

    elif choice == "4":
        print("\n" + report.generate("border"))

    elif choice == "5":
        print("Number of sections:", len(report))

    elif choice == "6":
        print("Total reports created:", Report.total_reports())

    elif choice == "7":
        print("Exiting Report Generator...")
        break

    else:
        print("Invalid choice!")
