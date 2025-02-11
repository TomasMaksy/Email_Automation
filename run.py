from main import send_email
import pandas as pd

# Set the subject of the email
subject = 'Test email'


# Load the path to the PDF file (attachment)
pdf_file_path = "./deleteme.pdf"



# Read the HTML content from the file
with open('index.html', 'r') as file:
    body = file.read()


# Load the data for recipients (Including their email addresses)
path_to_excel = "./recipients.xlsx"
recipients = pd.read_excel(path_to_excel)
print(f"To {len(recipients["Email"].to_list())} accounts")


# Load the template for the body of the email
with open('index.html', 'r') as file:
    template = file.read()


# Make sure that the user wants to continue
res = ""
while res != "y" or res != "n":
    res = input("Continue? Y/N: ").lower()
    if res == "y":
        for _, row in recipients.iterrows():
                    # Personalize the email content
                    personalized_body = template.replace("{{ name }}", row["Name"])  # Adjust column name
                    personalized_body = personalized_body.replace("{{ number }}", str(row["Phone Number"]))



                    send_email(row["Email"], subject, personalized_body, pdf_file_path, is_html=True)
                    print(f"Email to {row['Name']} sent!")
        break
    elif res == "n":
        print("Exiting...")
        exit()
    else:
        print("Invalid input. Please enter 'y' or 'n'.")



