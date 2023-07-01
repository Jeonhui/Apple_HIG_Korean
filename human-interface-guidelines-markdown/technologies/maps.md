Maps
====

A map displays outdoor or indoor geographical data in your app or on your website.![A sketch of a tri-fold map, suggesting navigation. The image is overlaid with rectangular and circular grid lines and is tinted blue to subtly reflect the blue in the original six-color Apple logo.](https://docs-assets.developer.apple.com/published/2438a971853ddedc25626eb9d276d71e/technologies-maps-intro@2x.png)

A map uses a familiar interface that supports much of the same functionality as the system-provided Maps app, such as zooming, panning, and rotation. A map can also include annotations and overlays and show routing information, and you can configure it to use a standard graphical view, a satellite image-based view, or a view that’s a hybrid of both.

[Best practices](/design/human-interface-guidelines/maps#Best-practices)
------------------------------------------------------------------------

**In general, make your map interactive.** People expect to be able to zoom, pan, and otherwise interact with maps in familiar ways. Noninteractive elements, such as overlays that obscure the map, can interfere with people’s expectations for how maps behave.

**Pick a map emphasis style that suits the needs of your app.** There are two emphasis styles to choose from:

* The *default* style presents a version of the map with fully saturated colors, and is a good option for most standard map applications without a lot of custom elements. This style is also useful for keeping visual alignment between your map and the Maps app, in situations when people might switch between them.
* The *muted* style, by contrast, presents a desaturated version of the map. This style is great if you have a lot of information-rich content that you want to stand out against the map.

See [Custom information](/design/human-interface-guidelines/maps#Custom-information)
 for additional guidance.

**Help people find your app’s content.** Consider offering a search feature combined with a way to filter locations by category. The search field for a shopping mall map, for example, might include filters that make it easy to find common store types, like clothing, housewares, electronics, jewelry, and toys.

**Clearly identify elements that people select.** When someone selects a specific area or other element on the map, use distinct styling like an outline and color variation to call attention to the selection.

**Cluster overlapping points of interest to improve map legibility.** A *cluster* uses a single pin to represent multiple points of interest within close proximity. As people zoom in on a map, clusters expand to progressively reveal individual points of interest.

**Help people see the Apple logo and legal link.** It’s fine when parts of your interface temporarily cover the logo and link, but don’t cover these elements all the time. To help you maintain the visibility of the Apple logo and legal link, follow these recommendations.

* Use adequate padding to separate the logo and link from the map boundaries and your custom controls. For example, it works well to use 7 points of padding on the sides of the elements and 10 points above and below them.
* Avoid causing the logo and link to move with your interface. It’s best when the Apple logo and legal link appear to be fixed to the map.
* If your custom interface can move relative to the map, use the lowest position of the custom element to determine the placement of the logo and link. For example, if your app lets people pull up a custom card from the bottom of the screen, place the Apple logo and legal link 10 points above the lowest resting position of the card.

Note

The Apple logo and legal link aren’t shown on maps that are smaller than 200x100 pixels.

[Custom information](/design/human-interface-guidelines/maps#Custom-information)
--------------------------------------------------------------------------------

**Use annotations that match the visual style of your app.** Annotations identify custom points of interest on your map. The default annotation marker has a red tint and a white pin icon. You can change the tint to match the color scheme of your app. You can also change the icon to a string or image, like a logo. An icon string can contain any characters, including Unicode characters, but keep it to two to three characters in length for readability. For developer guidance, see [`MKAnnotationView`](/documentation/mapkit/mkannotationview)
.

**If you want to display custom information that’s related to standard map features, consider making them independently selectable.** When you support selectable map features, the system treats Apple-provided features (including points of interest, territories, and physical features) independently from other annotations that you add. You can configure custom appearances and information to represent these features when people select them. For developer guidance, see [`MKMapFeatureOptions`](/documentation/mapkit/mkmapfeatureoptions)
.

**Use overlays to define map areas with a specific relationship to your content.**

* *Above roads*, the default level, places the overlay above roads but below buildings, trees, and other features. This is great for situations where you want people to have an idea of what’s below the overlay, while still clearly understanding that it’s a defined space.
* *Above labels* places the overlay above both roads and labels, hiding everything beneath it. This is useful for content that you want to be fully abstracted from the features of the map, or when you want to hide areas of the map that aren’t relevant.

**Make sure there’s enough contrast between custom controls and the map.** Insufficient contrast makes controls hard to see and can cause them to blend in with the map. Consider using a thin stroke or light drop shadow to help a custom control stand out, or applying blend modes to the map area to increase its contrast with the controls atop it.

[Indoor maps](/design/human-interface-guidelines/maps#Indoor-maps)
------------------------------------------------------------------

Apps connected with specific venues like shopping malls and stadiums can design custom interactive maps that help people locate and navigate to indoor points of interest. Indoor maps can include overlays that highlight specific areas, such as rooms, kiosks, and other locations. They can also include text labels, icons, and routes.

* [Example 1](#)
* [Example 2](#)
* [Example 3](#)
![A screenshot of a map on iPhone, displaying the San Jose International airport and the surrounding area. A card in the bottom half of the screen displays information and options, including the airport name and buttons for sharing, closing the card, navigating to the airport, calling the airport, visiting the airport's website, and more.](https://docs-assets.developer.apple.com/published/669a55f1fc7dd419351d60b4decfbbf5/indoor-maps-example1@2x.png)![A screenshot of a map on iPhone, displaying Terminal B at the San Jose International airport. Gate numbers are displayed above the terminal on the map. A minimized card containing information and options for the airport is visible at the bottom of the screen.](https://docs-assets.developer.apple.com/published/bd86841c0079e56b609826b4b97c24aa/indoor-maps-example2@2x.png)![A screenshot of a map on iPhone, displaying a close-up view of a terminal at the San Jose International airport. A security checkpoint, first aid stations, restrooms, an escalator, and a gate number are displayed on the map. A minimized card containing a search field and a Browse SJC button is visible at the bottom of the screen.](https://docs-assets.developer.apple.com/published/b36b5ea10535fbb6b42f3ca319bba1e7/indoor-maps-example3@2x.png)**Adjust map detail based on the zoom level.** Too much detail can cause a map to appear cluttered. Show large areas like rooms and buildings at all zoom levels. Then, progressively add more detailed features and labels as the map is zoomed in. An airport map might show only terminals and gates when zoomed out, but reveal individual stores and restrooms when zoomed in.

![A screenshot of a map on iPhone, zoomed in to show the location of an elevator in San Jose International airport. A minimized card containing information about the elevator is visible at the bottom of the screen.](https://docs-assets.developer.apple.com/published/b4dc405bf622e949194d8b8e4394ef9f/indoor-maps-elevator@2x.png)**Use distinctive styling to differentiate the features of your map.** Using color along with icons can help distinguish different types of areas, stores, and services, and make it easy for people to quickly find what they’re looking for.

**Offer a floor picker if your venue includes multiple levels.** A floor picker lets people quickly jump between floors. If you implement this feature, keep floor numbers concise for simplicity. In most cases, a list of floor numbers — rather than floor names — is sufficient.

**Include surrounding areas to provide context.** Adjacent streets, playgrounds, and other nearby locations can all help orient people when they use your map. If these areas are noninteractive, use dimming and a distinct color to make them appear supplemental.

![A screenshot of a map on iPhone, zoomed in to show the numbers and locations of some gates in a terminal at San Jose International airport. Other areas, including parking structures, are displayed without details. A minimized card containing a search field and a Browse SJC button is visible at the bottom of the screen.](https://docs-assets.developer.apple.com/published/222bc580a24623284ceb5a388d31521a/indoor-maps-surroundings@2x.png)**Consider supporting navigation between your venue and nearby transit points.** Make it easy to enter and exit your venue by offering routing to and from nearby bus stops, train stations, parking lots, garages, and other transit locations. You might also offer a way for people to quickly switch over to Apple Maps for additional navigation options.

**Limit scrolling outside of your venue.** This can help people avoid getting lost when they swipe too hard on your map. When possible, keep at least part of your indoor map visible onscreen at all times. To help people stay oriented, you may need to adjust the amount of scrolling you permit based on the zoom level.

**Design an indoor map that feels like a natural extension of your app.** Don’t try to replicate the appearance of Apple Maps. Instead, make sure area overlays, icons, and text match the visual style of your app.

You use a specific, distinct format to create indoor maps; to learn more, see [Indoor Mapping Data Format](https://register.apple.com/resources/imdf/)
.

[Platform considerations](/design/human-interface-guidelines/maps#Platform-considerations)
------------------------------------------------------------------------------------------

*No additional considerations for iOS, iPadOS, macOS, tvOS, or visionOS.*

### [watchOS](/design/human-interface-guidelines/maps#watchOS)

On Apple Watch, maps are static snapshots of geographic locations. Place a map in your interface at design time and show the appropriate region at runtime. The displayed region isn’t interactive; tapping it opens the Maps app on Apple Watch. You can annotate the map to highlight points of interest or other relevant information. The system lets you add up to five annotations to a map.

![A screenshot of a map on Apple Watch, displaying Apple Park and some of the surrounding area.](https://docs-assets.developer.apple.com/published/befea7e8b96bc123bfef582ba3857d64/maps-watch1@2x.png)**Fit the map interface element to the screen.** The entire element needs to be visible on the Apple Watch display without requiring scrolling.

**Show the smallest region that encompasses the points of interest.** The content within a map interface element doesn’t scroll, so all key content must be visible within the displayed region.

For developer guidance, see [`WKInterfaceMap`](/documentation/watchkit/wkinterfacemap)
.

[Resources](/design/human-interface-guidelines/maps#Resources)
--------------------------------------------------------------

#### [Developer documentation](/design/human-interface-guidelines/maps#Developer-documentation)

[MapKit](/documentation/mapkit)


[MapKit JS](/documentation/mapkitjs)


[`MKStandardMapConfiguration`](/documentation/mapkit/mkstandardmapconfiguration)


[`MKAnnotationView`](/documentation/mapkit/mkannotationview)


[`MKLocalSearch`](/documentation/mapkit/mklocalsearch)


[Apple Maps Server API](/documentation/applemapsserverapi)


[Indoor Mapping Data Format](https://register.apple.com/resources/imdf/)


[`WKInterfaceMap`](/documentation/watchkit/wkinterfacemap)


#### [Videos](/design/human-interface-guidelines/maps#Videos)

[![](https://devimages-cdn.apple.com/wwdc-services/images/124/0767C1AF-A19F-4F7C-9A8A-7EFFFD9FD214/6528_wide_250x141_1x.jpg) What's new in MapKit](https://developer.apple.com/videos/play/wwdc2022/10035) 
[![](https://devimages-cdn.apple.com/wwdc-services/images/124/3DCA0649-A5F9-4D12-BE9D-CAB428FDD71D/6495_wide_250x141_1x.jpg) Meet Apple Maps Server APIs](https://developer.apple.com/videos/play/wwdc2022/10006) 
[Change log](/design/human-interface-guidelines/maps#Change-log)
----------------------------------------------------------------



| Date | Changes |
| --- | --- |
| September 23, 2022 | Added guidelines for presenting custom information, refined best practices, and consolidated guidance into one page. |

