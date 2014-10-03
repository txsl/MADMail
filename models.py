from config import newerpol

from schema import t_MumsandDadsAllocation

EMAIL_POSTFIX = "@imperial.ac.uk"

def return_families(department):
    family_list = {}
    person_details = {}
    family_names = {}

    all_results = newerpol.query(t_MumsandDadsAllocation).filter_by(OCNameTypeName=department, CurrentYear=1)


    for res in all_results:
        person_details[res.FirstParentLogin] = (res.FirstParentFName, res.FirstParent)
        person_details[res.SecondParentLogin] = (res.SecondParentFName, res.SecondParent)
        person_details[res.Login] = (res.ChildFname, res.ChildName)

        couple = (res.FirstParentLogin, res.SecondParentLogin)
        try:
            family_list[couple].append(res.Login)
        except KeyError:
            family_list[couple] = [res.Login]

    for parents, children in family_list.iteritems():

        family_names[parents] = {}
        family_names[parents]['ParentFirstNames'] = person_details[parents[0]][0] + " and " + person_details[parents[1]][0]
        family_names[parents]['ParentFullNames'] = person_details[parents[0]][1] + " and " + person_details[parents[1]][1]
        family_names[parents]['ParentEmails'] = parents[0] + EMAIL_POSTFIX + ", " + parents[1] + EMAIL_POSTFIX

        num_children = len(children)

        child_names = ""
        for i in range(num_children - 2):
            child_names += person_details[children[i]][0] + ", "
        child_names += person_details[children[num_children - 2]][0] + " and " + person_details [children[num_children - 1]][0]
        family_names[parents]['ChildFirstNames'] = child_names

        child_names = ""
        for i in range(num_children - 2):
            child_names += person_details[children[i]][1] + ", "
        child_names += person_details[children[num_children - 2]][1] + " and " + person_details [children[num_children - 1]][1]
        family_names[parents]['ChildFullNames'] = child_names

        child_names = ""
        for i in range(num_children - 2):
            child_names += children[i] + EMAIL_POSTFIX + ", "
        child_names += children[num_children - 2] + EMAIL_POSTFIX + " and " + children[num_children - 1] + EMAIL_POSTFIX
        family_names[parents]['ChildEmails'] = child_names

    return family_list, family_names

if __name__ == "__main__":
    print return_families(u'Electrical & Electronic Engineering')