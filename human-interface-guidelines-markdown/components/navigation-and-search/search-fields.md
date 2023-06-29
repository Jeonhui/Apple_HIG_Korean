June 5, 2023

 Added guidance for using search fields in watchOS. Search fields
=============

A search field lets people search a collection of content for specific terms they enter.![A stylized representation of a search field containing placeholder text and a dictation icon. The image is tinted red to subtly reflect the red in the original six-color Apple logo.](https://docs-assets.developer.apple.com/published/1bb649a494afe216471bd9201277a977/components-search-field-intro@2x.png)

A search field is an editable text field that often displays a Search button, a Clear button, and optional placeholder text. Depending on the platform, a search text field can use a token to represent a search term that people enter or an app-defined item that people can use as a filter. A *token* uses a visual treatment that encapsulates the term or item, indicating that people can easily copy or drag the token without having to select the text within it. For an example of a token in macOS, see [Token fields](/design/human-interface-guidelines/token-fields)
.

[Best practices](/design/human-interface-guidelines/search-fields#Best-practices)
---------------------------------------------------------------------------------

**Consider providing hints to help guide searching.** For example, Music includes the placeholder text “Artists, Songs, Lyrics, and More” to suggest what people can search for. Avoid using a term like “Search” for placeholder text because it doesn’t provide any helpful information.

**Consider providing helpful shortcuts and other content near a search field.** For example, Safari shows bookmarks as soon as people tap or click the search field, letting them select a bookmark to open it immediately. For developer guidance, see [`UISearchSuggestion`](/documentation/uikit/uisearchsuggestion)
.

**Start the search at an appropriate time.** You can start the search as soon as people start typing, or wait until they choose Return or Enter. Searching while people type provides results that are continuously refined as the text becomes more specific. If the search happens after people finish typing, consider showing a menu while they type that lets them choose from their recent searches or terms you suggest.

**Include a Clear button.** People appreciate having a Clear button because it lets them quickly delete their current search terms.

**Take privacy into consideration before displaying search history.** People might not appreciate having their search history displayed where others might see it. As an alternative, consider offering a scope bar that helps people narrow down results quickly.

[Scope bars](/design/human-interface-guidelines/search-fields#Scope-bars)
-------------------------------------------------------------------------

In iOS, iPadOS, and tvOS, you can use a scope bar to help people refine the scope of a search. For developer guidance, see [`UISearchBar`](/documentation/uikit/uisearchbar)
.

![A partial screenshot of Mail on iPhone, highlighted to show a scope bar displaying the label All Mailboxes on the left and the label Current Mailbox on the right.](https://docs-assets.developer.apple.com/published/76adbb3a79d288f53c3a4ee3527fa81a/scope-bar-ios@2x.png)**Favor improving search results over including a scope bar.** A scope bar can be useful when there are clearly defined categories for the search, but it’s generally better to improve search results so scoping isn’t necessary.

[Platform considerations](/design/human-interface-guidelines/search-fields#Platform-considerations)
---------------------------------------------------------------------------------------------------

*No additional considerations for visionOS*

### [iOS, iPadOS](/design/human-interface-guidelines/search-fields#iOS-iPadOS)

You can display a search field in a navigation bar or within your content area. When you use system-provided components to include a search field in a navigation bar, it automatically receives the appropriate appearance and behaves as people expect. For example, the search bar can hide until people swipe down to reveal it.

Developer note

Use [`searchController`](/documentation/uikit/uinavigationitem/2897305-searchcontroller)
 if you want to take advantage of the system-provided appearance and behavior of a search field within a navigation bar. If you need to implement custom appearances and behaviors for a search field, consider using [`UISearchBar`](/documentation/uikit/uisearchbar)
 to create a field you want to put in a bar or [`UISearchTextField`](/documentation/uikit/uisearchtextfield)
 to apply a custom background to a search field in a content area.

### [macOS](/design/human-interface-guidelines/search-fields#macOS)

Although it’s typical to include a search field in a window’s toolbar, you can also display one in the body area.

**Avoid supplying an introductory label for a search field within a content area.** People are familiar with the distinctive appearance of a search field, so there is no need to label it. In contrast, when you place a search field in a toolbar, supply the label “Search” so that the label appears when people configure the toolbar to show icons and text or text only.

**Apply the appropriate bezel style to a scope button.** There are two bezel styles you can use. The *recessed* bezel — which makes the button look like it’s slightly inset — is for scope buttons that toggle on and off to narrow focus; the *rounded* bezel is for scope buttons that initiate an action or specify search criteria.

![A partial screenshot of a Finder window with callouts to the Desktop scope button (the callout text is \"Recessed\") and the Save button (the callout text is \"Rounded\").](https://docs-assets.developer.apple.com/published/43cbf9254d911e2dada4c18bce8a9ce9/scope-buttons-macos@2x.png)

**If appropriate, let people refine the scope.** You can provide supplementary scoping rules using filter rows that appear beneath a scope bar. For example, when searching for a filename in Finder, people can click an Add (+) button to specify additional attributes like an extension or a modification date range. A filter row can include text fields, buttons, and other controls for specifying filter criteria.

![A partial screenshot of a Finder window in which name and last opened date scope buttons have been set so that a file named \"landscape.png\" has been found.](https://docs-assets.developer.apple.com/published/f725f8ebf869b64af61e5086024bc898/scope-bar-macos-additional@2x.png)

### [tvOS](/design/human-interface-guidelines/search-fields#tvOS)

A search screen is a specialized keyboard screen that helps people enter search text, displaying search results beneath the keyboard in a fully customizable view. For developer guidance, see [`UISearchController`](/documentation/uikit/uisearchcontroller)
.

**Consider presenting recent searches.** Because people frequently repeat searches in tvOS, you can minimize the need for text entry by listing popular or recent searches in the results area under the keyboard before people start typing.

**Provide suggestions to make searching easier.** People typically don’t want to do a lot of typing in tvOS. To improve the search experience, provide popular and context-specific search suggestions, including recent searches when available. For developer guidance, see [Using Suggested Searches with a Search Controller](/documentation/uikit/view_controllers/using_suggested_searches_with_a_search_controller)
.

**Simplify search results.** Avoid providing a lengthy list of search results that requires lots of scrolling. In addition to prioritizing the most likely results, consider categorizing them to help people find what they want.

**Consider letting people filter search results.** For example, you can include a scope bar in the search results content area to help people quickly and easily filter search results.

### [watchOS](/design/human-interface-guidelines/search-fields#watchOS)

You can display a search field in a [toolbar](https://developer.apple.com/design/human-interface-guidelines/components/menus-and-actions/toolbars)
. The system hides the search bar until people swipe down to reveal it.

![An illustration representing an Apple Watch screen that includes a search field and a list of buttons.](https://docs-assets.developer.apple.com/published/1bb58256a7012836df396a053e94f58a/search-fields-watch@2x.png)

When someone taps the search field, the system displays a text-input control.

![An illustration representing an Apple Watch screen that includes a keyboard for entering search text.](https://docs-assets.developer.apple.com/published/9a70e1accafa350fbf68921f9f1bc677/search-fields-watch-input@2x.png)

**Provide suggestions to make searching easier.** People typically don’t want to do a lot of typing in watchOS. To improve the search experience, offer popular and context-specific search suggestions, including recent searches when available. For developer guidance, see [`searchSuggestions(_:)`](/documentation/SwiftUI/View/searchSuggestions(_:))
.

[Resources](/design/human-interface-guidelines/search-fields#Resources)
-----------------------------------------------------------------------

#### [Related](/design/human-interface-guidelines/search-fields#Related)

[Searching](/design/human-interface-guidelines/searching)


#### [Developer documentation](/design/human-interface-guidelines/search-fields#Developer-documentation)

[`searchable(text:placement:)`](/documentation/SwiftUI/View/searchable(text:placement:))


[`UISearchBar`](/documentation/uikit/uisearchbar)


[`UISearchTextField`](/documentation/uikit/uisearchtextfield)


[`NSSearchField`](/documentation/appkit/nssearchfield)


#### [Videos](/design/human-interface-guidelines/search-fields#Videos)

[![](https://devimages-cdn.apple.com/wwdc-services/images/119/BE8FF113-0FE1-40FC-86BF-FE95BE2FF7A5/5027_wide_250x141_1x.jpg) Discoverable design](https://developer.apple.com/videos/play/wwdc2021/10126) 
[![](https://devimages-cdn.apple.com/wwdc-services/images/119/D45C244B-2038-4692-99A0-6131ED5FD984/5084_wide_250x141_1x.jpg) Craft search experiences in SwiftUI](https://developer.apple.com/videos/play/wwdc2021/10176) 
[Change log](/design/human-interface-guidelines/search-fields#Change-log)
-------------------------------------------------------------------------



| Date | Changes |
| --- | --- |
| June 5, 2023 | Added guidance for using search fields in watchOS. |

