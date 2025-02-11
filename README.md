# Email Automation Pipeline

This pipeline is designed to **speed up the process of sending hundreds of similar emails** in a matter of minutes

# Files

**recipients.xlsx** - An excel file storing the main information about your recipients. 

**index.html** - A file that contains the main structure and text of your email's body. If you want to personalize each email to their recipients, you can insert placeholders in this file by using e.g. {{ name }}.

**main.py** - contains the boring code responsible for actually sending the emails and making sure that your **.pdf attachments** get sent

**run.py** - This is the file, where most of the logic happens
You specify the subject of you email on line 5:
`subject = 'Type the subject here'`
You also specify a pdf file path that you want to attach to every email
`pdf_file_path = './filename.pdf'`

The last thing you need to change in this file are the placeholders that you placed in the html file. You can now pull the value of a certain column from the excel file specific to that email. e.g.:
`row["Name"]`
and you can use it with the following line:
`personalized_body  =  template.replace("{{ name }}", row["Name"])`


**.env** - a secret file that you need in order to securely store your email credentials. It should contain two variables:
`SENDER_EMAIL = youremail@gmail.com`
`SENDER_PASSWORD = AAAABBBBCCCCDDDD` - 16 digit app-specific password can be generated [here](https://myaccount.google.com/apppasswords?continue=https://myaccount.google.com/security?gar=WzEyMF0&hl=en&utm_source=OGB&utm_medium=act&rapt=AEjHL4OKWXKOWXjlNQ89fiCo9qhxdti7wBqfD9d8XXAitU2C_7yPLquW64vUQb_VXpHjM8b5QjAgB9SKvJOWBdiaDIvh4VcIO8IhGvT5-gjy43VYx9Joskk)




> **Note:** Make sure to send a test email first in order to avoid spamming the recipients

### How to run?
`python run.py`
> **Note:** There is a little check to minimize the number of human errors. A number of recipients will be displayed and the user will be prompted for confirmation. 
> Y - yes/confirm
> N - no/abort
