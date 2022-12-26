# **[technologies-carplay] system-elements**

## **Action sheets**

An action sheet is a specific style of alert that slides up from the bottom of the screen in response to a control or action, and presents a set of two or more choices related to the current context.

![https://developer.apple.com/design/human-interface-guidelines/technologies/carplay/images/ActionSheet_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/carplay/images/ActionSheet_2x.png)

**Avoid displaying action sheets in CarPlay.** Action sheets disrupt the user experience and increase the complexity of your app. It's fine to offer action sheets on iPhone, but avoid displaying them in CarPlay.

For related design guidance, see [Alerts](https://developer.apple.com/design/human-interface-guidelines/technologies/carplay/system-elements#alerts).

# **Activity indicators**

Don’t show a static or an empty screen while your app loads content. Use an activity indicator to let people know your app isn’t stalled.

![https://developer.apple.com/design/human-interface-guidelines/technologies/carplay/images/Activity_Spinner_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/carplay/images/Activity_Spinner_2x.png)

**If it’s helpful, provide useful information while waiting for a task to complete.** Include a label above an activity indicator to give extra context. Avoid vague terms like loading because they don’t usually add any value.

For developer guidance, see [UIActivityIndicatorView](https://developer.apple.com/documentation/uikit/uiactivityindicatorview).

# **Alerts**

Alerts convey important information related to the state of your app. An alert consists of a title, an optional message, and one or more buttons. Aside from these configurable elements, the visual appearance of an alert is static and can’t be customized.

![https://developer.apple.com/design/human-interface-guidelines/technologies/carplay/images/Alert_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/carplay/images/Alert_2x.png)

**Minimize alerts.** Alerts disrupt the user experience. Use alerts only for important situations like notifying people about problems. The infrequency of alerts helps ensure that people take them seriously.

For developer guidance, see [UIAlertController](https://developer.apple.com/documentation/uikit/uialertcontroller).

### **Alert titles and messages**

**Write short, descriptive, multiword alert titles.** The less text people have to read onscreen, the better. Try to craft a title that avoids adding extra text as a message. Because single-word titles rarely provide useful information, consider asking a question or using short sentences. Whenever possible, keep titles to a single line. Use sentence-style capitalization and appropriate punctuation for complete sentences. Don’t use ending punctuation for sentence fragments.

**If you must provide a message, write short, complete sentences.** Try to keep messages short enough to fit on one or two lines to prevent scrolling. Use sentence-style capitalization and appropriate punctuation.

**Avoid sounding accusatory, judgmental, or insulting.** People know that alerts notify them about problems and dangerous situations. As long as you use a friendly tone, it’s better to be negative and direct than positive and oblique. Avoid pronouns such as *you*, *your*, *me*, and *my*, which are sometimes interpreted as insulting or patronizing.

**Avoid explaining the alert buttons.** If your alert text and button titles are clear, you don't need to explain what the buttons do. In rare cases where you must provide guidance, use the word *tap*, preserve capitalization when referencing buttons, and don’t enclose button titles in quotes.

### **Alert buttons**

**Generally, use two-button alerts.** Two-button alerts provide an easy choice between two alternatives. Single-button alerts inform, but give no control over the situation. Alerts with three or more buttons create complexity and can require scrolling, which is a bad user experience. If you need more than two choices, consider using an action sheet instead. See [Action sheets](https://developer.apple.com/design/human-interface-guidelines/technologies/carplay/system-elements#action-sheets).

**Give alert buttons succinct, logical titles.** The best button titles consist of one or two words that describe the result of selecting the button. Use title-style capitalization and no ending punctuation. To the extent possible, use verbs and verb phrases that relate directly to the alert title and message. Use *OK* for simple acceptance. Avoid using *Yes* and *No*.

**Place commonly used buttons on the right and Cancel buttons on the left.** Typically, buttons people are most likely to tap are on the right. Cancel buttons should always be on the left.

**Label cancellation buttons appropriately.** A button that cancels an alert’s action should always be labeled Cancel.

**Identify destructive buttons.** If an alert button results in a destructive action, such as deleting content, set the button’s style to Destructive so that it gets appropriate formatting by the system. For developer guidance, see the [UIAlertActionStyleDestructive](https://developer.apple.com/documentation/uikit/uialertactionstyle/uialertactionstyledestructive) constant of [UIAlertAction](https://developer.apple.com/documentation/uikit/uialertaction). Additionally, provide a Cancel button so people can safely opt out of the destructive action. Make the Cancel button bold by marking it as the default button.

**Allow the Home button to cancel alerts.** Tapping Home while an alert is visible exits the app. It should also produce the same effect as tapping the Cancel button—that is, the alert is dismissed without performing any action. If your alert doesn’t have a Cancel button, consider implementing a cancel action in your code that runs when the Home button is tapped.

# **Buttons**

Buttons initiate app-specific actions when tapped, have customizable backgrounds, and can include a title or an icon. Although iOS provides a number of predefined button styles, CarPlay supports only the system button style.

![https://developer.apple.com/design/human-interface-guidelines/technologies/carplay/images/Button_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/carplay/images/Button_2x.png)

### **System buttons**

System buttons often appear in navigation bars, but may be used anywhere.

**Use verbs in titles.** An action-specific title, such as Add Favorite, shows that a button is interactive and says what happens when you tap it.

**Use title-case for titles.** Capitalize every word except articles, coordinating conjunctions, and prepositions of four or fewer letters.

**Keep titles short.** Overly long text can crowd your interface and may get truncated on smaller screens.

**Consider adding a border or a background only when necessary.** By default, a button has no border or background. In some content areas, however, a border or background is necessary to denote interactivity. In the Phone app, bordered number keys reinforce the traditional model of making a call, and the background of the Call button provides an eye-catching target that’s easy to hit.

For developer guidance, see the [UIButtonTypeSystem](https://developer.apple.com/documentation/uikit/uibuttontype/uibuttontypesystem) button type of [UIButton](https://developer.apple.com/documentation/uikit/uibutton).

# **Collections**

A collection manages an ordered set of content, such as a set of Internet radio station logos, and presents it in a highly visual layout. Because a collection doesn’t enforce a strictly linear format, it’s particularly well-suited to displaying items that vary in size. Generally speaking, collections are ideal for showing off image-based content. Optionally, implement backgrounds and other decorative views to visually distinguish subsets of items.

Collections support both interactivity and animation. By default, you can tap to select, touch and hold to edit, and swipe to scroll. If your app requires it, you can add more gestures for custom actions. Within a collection, animations can be enabled whenever items are inserted, deleted, or reordered, and custom animations are also supported.

**Avoid creating radical new designs when a standard row or grid layout is sufficient.** A collection should enhance the user experience, not become the center of attention. Make it easy to select an item. If it’s hard to tap an item in your collection, people will get frustrated and lose interest before reaching the content they want. Use adequate padding around content to keep the layout clean and prevent overlapping.

**Consider using a table instead of a collection for text.** It’s generally simpler and more efficient to view and digest textual information when it’s displayed in a scrollable list.

**Use caution when making dynamic layout changes.** The layout of a collection can be changed at any time. If you dynamically change the layout while people are viewing and interacting with it, be sure the change makes sense and is easy to track. Unmotivated layout changes can make your app seem unpredictable and difficult to use. If context is lost due to a layout change, people are likely to feel like they’re no longer in control.

For developer guidance, see [UICollectionView](https://developer.apple.com/documentation/uikit/uicollectionview).

# **Labels**

A label describes an onscreen interface element or provides a short message. Labels can display any amount of static text, but are best kept short.

![https://developer.apple.com/design/human-interface-guidelines/technologies/carplay/images/Label_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/carplay/images/Label_2x.png)

**Keep labels legible.** Labels can include plain or styled text. If you adjust the style of a label or use custom fonts, be sure not to sacrifice legibility.

For developer guidance, see [UILabel](https://developer.apple.com/documentation/uikit/uilabel).

# **Navigation bars**

A navigation bar appears at the top of an app screen, and enables navigation through a series of hierarchical app screens. When a new screen is displayed, a back button, preceded by a chevron and often labeled with the title of the previous screen, appears on the left side of the bar. Sometimes, the right side of a navigation bar contains a control, such as a Search button, for interacting with the active view.

![https://developer.apple.com/design/human-interface-guidelines/technologies/carplay/images/Navigation_Bar_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/carplay/images/Navigation_Bar_2x.png)

**Consider showing the title of the current view in the navigation bar.** In most cases, a title provides context by letting people know what they’re looking at. However, if titling a navigation bar seems redundant, you can leave the title empty. For example, the Now Playing screen in the Music app doesn’t include a title in the navigation bar because the rest of the screen provides sufficient context.

**Avoid crowding a navigation bar with too many controls.** In general, a navigation bar should contain no more than the view’s current title, a back button, and one or two controls for interacting with the view’s contents.

**Don’t include multisegment breadcrumb paths.** The back button always performs a single action—returning to the previous screen. If you think people might get lost without the full path to the current screen, consider flattening your app’s hierarchy.

**Give text-titled buttons enough room.** If your navigation bar includes multiple text buttons, the text of those buttons may appear to run together, making the buttons indistinguishable. Add separation by inserting a fixed space item between the buttons. For developer guidance, see the [UIBarButtonSystemItemFixedSpace](https://developer.apple.com/documentation/uikit/uibarbuttonsystemitem/uibarbuttonsystemitemfixedspace) constant value in [UIBarButtonItem](https://developer.apple.com/documentation/uikit/uibarbuttonitem).

**Use the standard back button.** People know that the standard back button lets them retrace steps through a hierarchy of information.

For developer guidance, see [UINavigationBar](https://developer.apple.com/documentation/uikit/uinavigationbar).

# **Scroll views**

A scroll view lets users browse content that’s larger than the visible area. As a user swipes, flicks, drags, and taps, a scroll view follows the gesture, revealing or zooming content in a way that feels natural. A scroll view itself has no appearance, but does display transient scrolling indicators as people interact with it. A scroll view can also be configured to operate in paging mode, where scrolling reveals an entirely new page of content rather than moving around the current page.

**Don’t place a scroll view inside another scroll view.** Doing so creates an unpredictable interface that’s difficult to control.

**In general, display one scroll view at a time.** People often make large swipe gestures when scrolling, and it can be hard to avoid interacting with a neighboring scroll view on the same screen. If you need to put two scroll views on one screen, consider allowing them to scroll in different directions so one gesture is less likely to affect both views.

For developer guidance, see [UIScrollView](https://developer.apple.com/documentation/uikit/uiscrollview).

# **Tab bars**

A tab bar appears at the top of an app screen, enabling users to quickly switch between different sections of an app. A tab bar may contain any number of tabs, but the number of visible tabs varies based on the display size. If some tabs can’t be displayed due to limited horizontal space, the final visible tab becomes a More tab, which lists additional tabs on a separate screen.

![https://developer.apple.com/design/human-interface-guidelines/technologies/carplay/images/Tab_Bar_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/carplay/images/Tab_Bar_2x.png)

**In general, use a tab bar to flatten your information hierarchy.** A tab bar provides access to several peer information categories or modes at once.

**Don’t remove or disable a tab when its function is unavailable.** If tabs are available in some cases but not in others, your app’s interface appears unstable and unpredictable. Ensure that all tabs are always enabled. Explain why a tab’s content is unavailable in the body of the tab.

**Use a tab bar strictly for navigation.** Tab bar buttons should not be used to perform actions.

**In general, use between three and five tabs.** Each additional tab reduces the tappable area for selecting a tab and increases the complexity of your app, making it harder to locate information. Although a More tab can display extra tabs, this requires additional taps and is a poor use of space. Include essential tabs only, and use the minimum tabs necessary for your information hierarchy. Too few tabs can be a problem too, as it can make your interface appear disconnected.

**Use badging to communicate unobtrusively.** You can display a badge—a red oval containing white text and either a number or an exclamation point—on a tab to indicate that new information is associated with that view or mode.

For developer guidance, see [UITabBar](https://developer.apple.com/documentation/uikit/uitabbar).

# **Tables**

A table presents data as a scrolling, single-column list of rows. Use a table to display large or small amounts of information cleanly and efficiently in the form of a list.

![https://developer.apple.com/design/human-interface-guidelines/technologies/carplay/images/Table_Index_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/carplay/images/Table_Index_2x.png)

**Consider table width.** Thin tables can cause truncation and wrapping, making them hard to read and scan quickly at a distance.

**Begin showing table content quickly.** Don’t wait for extensive table content to load before showing something. Fill onscreen rows with textual data immediately and show more complex data—such as images—as it becomes available. This technique gives people useful information right away and increases the perceived responsiveness of your app. In some cases, showing stale, older data may make sense until fresh, new data arrives.

**Communicate progress as content loads.** If a table’s data takes time to load, show a spinning activity indicator to reassure people that your app is still running.

**Update table content regularly to reflect newer data, but don’t change the scrolling position.** Add new content to the beginning or end of the table, and let people scroll to it when they’re ready. Some apps display an indicator when new data has been added, and provide a control for jumping right to it.

For developer guidance, see [UITableView](https://developer.apple.com/documentation/uikit/uitableview).

### **Table rows**

You use standard table cell styles to define how content appears in table rows.

![https://developer.apple.com/design/human-interface-guidelines/technologies/carplay/images/Table_Row-default_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/carplay/images/Table_Row-default_2x.png)

**Default.** An optional image on the left side of the row, followed by a left-aligned title. It’s a good option for displaying items that don’t require supplementary information. For developer guidance, see the [UITableViewCellStyleDefault](https://developer.apple.com/documentation/uikit/uitableviewcellstyle/uitableviewcellstyledefault) constant of [UITableViewCell](https://developer.apple.com/documentation/uikit/uitableviewcell).

![https://developer.apple.com/design/human-interface-guidelines/technologies/carplay/images/Table_Row_sub_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/carplay/images/Table_Row_sub_2x.png)

**Subtitle.** A left-aligned title on one line and a left-aligned subtitle on the next. This style works well in a table where rows are visually similar. The additional subtitle helps distinguish rows from one another. For developer guidance, see the [UITableViewCellStyleSubtitle](https://developer.apple.com/documentation/uikit/uitableviewcellstyle/uitableviewcellstylesubtitle) constant of [UITableViewCell](https://developer.apple.com/documentation/uikit/uitableviewcell).

![https://developer.apple.com/design/human-interface-guidelines/technologies/carplay/images/Table_Row-V1_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/carplay/images/Table_Row-V1_2x.png)

**Value 1.** A left-aligned title with a right-aligned subtitle in a lighter font on the same line. For developer guidance, see the [UITableViewCellStyleValue1](https://developer.apple.com/documentation/uikit/uitableviewcellstyle/uitableviewcellstylevalue1) constant of [UITableViewCell](https://developer.apple.com/documentation/uikit/uitableviewcell).

![https://developer.apple.com/design/human-interface-guidelines/technologies/carplay/images/Table_Row-V2_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/carplay/images/Table_Row-V2_2x.png)

**Value 2.** A right-aligned title, followed by a left-aligned subtitle in a lighter font on the same line. For developer guidance, see [UITableViewCellStyleValue2](https://developer.apple.com/documentation/uikit/uitableviewcellstyle/uitableviewcellstylevalue2) constant of [UITableViewCell](https://developer.apple.com/documentation/uikit/uitableviewcell).

**Keep text succinct to avoid clipping.** Truncated words and phrases are hard to scan and decipher. Text truncation is automatic in all table cell styles, but it can present more or less of a problem depending on which cell style you use and where truncation occurs.

**Provide feedback when a selection is made.** People expect a row to highlight briefly when its content is tapped. Then, people expect a new view to appear or something to change, such as a checkmark appearing, that indicates a selection has been made.

**Design a custom table cell style for nonstandard table rows.** Standard styles are great for use in a variety of common scenarios, but some content or your overall app design may call for a heavily customized table appearance.

For developer guidance, see [UITableViewCell](https://developer.apple.com/documentation/uikit/uitableviewcell).

# **Text views**

A text view displays multiline, styled text content. Text views can be any height and enable scrolling when the content extends outside of the view. By default, content within a text view is left-aligned and uses the system typeface in white. CarPlay doesn’t support text editing and selection.

![https://developer.apple.com/design/human-interface-guidelines/technologies/carplay/images/Textview_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/carplay/images/Textview_2x.png)

**Keep text legible.** Although you can use multiple fonts, colors, and alignments in creative ways, it’s essential to maintain the readability of your content. Be sure to test your text legibility at different times of day.

For developer guidance, see [UITextView](https://developer.apple.com/documentation/uikit/uitextview).

# **Web views**

A web view loads and displays rich, static content, such as HTML embedded within your app.

**Use a web view to present static content only.** Do not use a web view to display dynamic content or to offer web browsing capabilities.

For developer guidance, see [WKWebView](https://developer.apple.com/documentation/webkit/wkwebview).