# **[patterns] searching**

# People use various search techniques to find content on their device, within an app, and within a document or file.

![https://developer.apple.com/design/human-interface-guidelines/images/intro/patterns/pattern-searching-intro-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/patterns/pattern-searching-intro-dark_2x.png)

To search for content within an app, people generally expect to use a search bar. When it makes sense, you can personalize the search experience by using what you know about how people interact with your app. For example, you might display recent searches or a search history, or offer search-term suggestions, completions, or corrections based on terms people searched earlier in your app. For guidance, see [Search fields](https://developer.apple.com/design/human-interface-guidelines/components/navigation-and-search/search-fields).

In some cases, people appreciate the ability to scope a search or filter the results. For example, people might want to search for items by specifying attributes like creation date, file size, or file type. For guidance, see [Scope bars](https://developer.apple.com/design/human-interface-guidelines/components/navigation-and-search/search-fields/#scope-bars). You can also help people find content within an open document or file by implementing ways to find content in a window or page in your iOS, iPadOS, or macOS app.

In iOS, iPadOS, and macOS, Spotlight helps people find content across all apps in the system and on the web. When you index and provide information about your app’s content, people can use Spotlight to find content your app contains without opening it first.

# **Best practices**

**Make your app’s content searchable.** You can share content with Spotlight by making it indexable and specifying descriptive attributes known as *metadata*. Spotlight extracts, stores, and organizes this information to allow for fast, comprehensive searches.

**Define metadata for custom file types you handle.** Supply a Spotlight File Importer plug-in that describes the types of metadata your file format contains. For developer guidance, see [CSImportExtension](https://developer.apple.com/documentation/corespotlight/csimportextension).

**Use Spotlight to offer advanced file-search capabilities within the context of your app.** For example, you might include a button that instantly initiates a Spotlight search based on the current selection. You might then display a custom view that presents the search results or a filtered subset of them.

**Prefer using the system-provided open and save views.** The system-provided open and save views generally include a built-in search field that people can use to search and filter the entire system. For related guidance, see [File management](https://developer.apple.com/design/human-interface-guidelines/patterns/file-management).

**Implement a Quick Look generator if your app produces custom file types.** A Quick Look generator helps Spotlight and other apps show previews of your documents. For developer guidance, see [Quick Look](https://developer.apple.com/documentation/quicklook/).

# **Platform considerations**

*No additional considerations for iOS, iPadOS, macOS, tvOS, or watchOS.*