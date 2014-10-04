import time

from jinja2 import Environment, PackageLoader
from flask import Markup

from models import return_families, return_emails_to_send, dept_id_to_name, mark_merge_as_sent
from helpers import BatchMail, strip_tags, send_mail, send_via_smtplib

env = Environment(loader=PackageLoader('cron', 'templates'))

MERGE_MAPPINGS = {
    "!PARENTFIRSTNAMES!": "ParentFirstNames",
    "!PARENTSFULLNAMES!": "ParentFullNames",
    "!CHILDFIRSTNAMES!": "ChildFirstNames",
    "!CHILDFULLNAMES!": "ChildFullNames",
    "!PARENTEMAILS!": "ParentEmails",
    "!CHILDEMAILS!": "ChildEmails",
}

TEMPLATE = 'email.html'

emails_to_send = return_emails_to_send()

for email in emails_to_send:

    mark_merge_as_sent(email)

    dept_name = dept_id_to_name(email.DepartmentId)
    family_list, family_names, family_emails = return_families(dept_name)

    mail = BatchMail()
    print "Number of emails to send: %s" % (len(family_list),)
    for parents, children in family_list.iteritems():

        merged_content = email.Content

        for tag, data in MERGE_MAPPINGS.iteritems():
            merged_content = merged_content.replace(tag, family_names[parents][data])

        send_to = []

        if email.email_parents:
            send_to = family_emails[parents]['Parents']
        if email.email_children:
            send_to = send_to + family_emails[parents]['Children']

        print send_to

        # Comment when deployed hashtag safetyfirst hashtag alwaysuseprotection
        # send_to = ['txl11@ic.ac.uk']

        # Time for templating
        template = env.get_template(TEMPLATE)
        output = template.render(content=Markup(merged_content), top_text=email.top_text)
        text_output = strip_tags(merged_content)


        mail.queue_mail(email.Subject, ("Mums and Dads", "mumsanddads@imperial.ac.uk"),
                        send_to, html_body=output, text_body=text_output)

        # Comment when deployed hashtag safetyfirst hashtag alwaysuseprotection
        # break

    mail.send_queue()


"""
The following tags will work:
!PARENTFIRSTNAMES!
!PARENTSFULLNAMES!
!CHILDFIRSTNAMES!
!CHILDFULLNAMES!
!PARENTEMAILS!
!CHILDEMAILS!
"""

