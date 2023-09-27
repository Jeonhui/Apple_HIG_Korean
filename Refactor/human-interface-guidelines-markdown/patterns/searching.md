Searching
=========

People use various search techniques to find content on their device, within an app, and within a document or file.![A sketch of a magnifying glass, suggesting the search for information. The image is overlaid with rectangular and circular grid lines and is tinted orange to subtly reflect the orange in the original six-color Apple logo.](https://docs-assets.developer.apple.com/published/d80bc4d95013730b824dc7956f912b4d/patterns-searching-intro@2x.png)

To search for content within an app, people generally expect to use a search bar. When it makes sense, you can personalize the search experience by using what you know about how people interact with your app. For example, you might display recent searches or a search history, or offer search-term suggestions, completions, or corrections based on terms people searched earlier in your app. For guidance, see [Search fields](/design/human-interface-guidelines/search-fields)
.

In some cases, people appreciate the ability to scope a search or filter the results. For example, people might want to search for items by specifying attributes like creation date, file size, or file type. For guidance, see [Scope bars](/design/human-interface-guidelines/search-fields#Scope-bars)
. You can also help people find content within an open document or file by implementing ways to find content in a window or page in your iOS, iPadOS, or macOS app.

In iOS, iPadOS, and macOS, Spotlight helps people find content across all apps in the system and on the web. When you index and provide information about your app’s content, people can use Spotlight to find content your app contains without opening it first.

[Best practices](/design/human-interface-guidelines/searching#Best-practices)
-----------------------------------------------------------------------------

**Make your app’s content searchable.** You can share content with Spotlight by making it indexable and specifying descriptive attributes known as *metadata*. Spotlight extracts, stores, and organizes this information to allow for fast, comprehensive searches.

**Define metadata for custom file types you handle.** Supply a Spotlight File Importer plug-in that describes the types of metadata your file format contains. For developer guidance, see [`CSImportExtension`](/documentation/corespotlight/csimportextension)
.

**Use Spotlight to offer advanced file-search capabilities within the context of your app.** For example, you might include a button that instantly initiates a Spotlight search based on the current selection. You might then display a custom view that presents the search results or a filtered subset of them.

**Prefer using the system-provided open and save views.** The system-provided open and save views generally include a built-in search field that people can use to search and filter the entire system. For related guidance, see [File management](/design/human-interface-guidelines/file-management)
.

**Implement a Quick Look generator if your app produces custom file types.** A Quick Look generator helps Spotlight and other apps show previews of your documents. For developer guidance, see [QuickLook](/documentation/quicklook)
.

[Platform considerations](/design/human-interface-guidelines/searching#Platform-considerations)
-----------------------------------------------------------------------------------------------

*No additional considerations for iOS, iPadOS, macOS, tvOS, visionOS, or watchOS.*

[Resources](/design/human-interface-guidelines/searching#Resources)
-------------------------------------------------------------------

#### [Related](/design/human-interface-guidelines/searching#Related)

[Search fields](/design/human-interface-guidelines/search-fields)


#### [Developer documentation](/design/human-interface-guidelines/searching#Developer-documentation)

[Making Content Searchable](/documentation/corespotlight/making_content_searchable)


#### [Videos](/design/human-interface-guidelines/searching#Videos)

[![](https://devimages-cdn.apple.com/wwdc-services/images/124/6E076CE0-7DDF-4471-B6F0-005ADF9C7960/6500_wide_250x141_1x.jpg) What’s new in iPad app design](https://developer.apple.com/videos/play/wwdc2022/10009) 
[![](https://devimages-cdn.apple.com/wwdc-services/images/119/D45C244B-2038-4692-99A0-6131ED5FD984/5084_wide_250x141_1x.jpg) Craft search experiences in SwiftUI](https://developer.apple.com/videos/play/wwdc2021/10176) 
[![](https://devimages-cdn.apple.com/wwdc-services/images/119/293EC8B4-DE5B-4879-B0BD-5E6A11CFD7FD/4994_wide_250x141_1x.jpg) Showcase app data in Spotlight](https://developer.apple.com/videos/play/wwdc2021/10098) 
