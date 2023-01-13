# **[technologies] photo-editing**

# Photo-editing extensions let people modify photos and videos within the Photos app by applying filters or making other changes.

![https://developer.apple.com/design/human-interface-guidelines/images/intro/technologies/technology-photo-editing-intro_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/technologies/technology-photo-editing-intro_2x.png)

Edits are always saved in the Photos app as new files, safely preserving the original versions.

To access a photo editing extension, a photo must be in edit mode. While in edit mode, tapping the extension icon in the toolbar displays an action menu of available editing extensions. Selecting one displays the extension’s interface in a modal view containing a navigation bar. Dismissing this view confirms and saves the edit, or cancels it and returns to the Photos app.

# **Best practices**

**Confirm cancellation of edits.** Editing a photo or video can be time consuming. If someone taps the Cancel button, don’t immediately discard their changes. Ask them to confirm that they really want to cancel, and inform them that any edits will be lost after cancellation. There’s no need to show this confirmation if no edits have been made yet.

**Don’t provide a custom navigation bar.** Your extension loads within a modal view that already includes a navigation bar. Providing a second navigation bar is confusing and takes space away from the content being edited.

**Let people preview edits.** It’s hard to approve an edit if you can’t see what it looks like. Let people see the result of their work before closing your extension and returning to the Photos app.

**Use your app icon for your photo editing extension icon.** This instills confidence that the extension is in fact provided by your app.