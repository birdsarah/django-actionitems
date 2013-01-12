from forms import ActionItemUpdateForm

# In the future this will pull in data from external managers, 
# for now it just adds the word 'sync' to the ActionItem description
def sync(actionitem):
    f = ActionItemUpdateForm(instance=actionitem)
    actionitem = f.save(commit=False)
    actionitem.description += ' sync'
    actionitem.save()
    return actionitem
