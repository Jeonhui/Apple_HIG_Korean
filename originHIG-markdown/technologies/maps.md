# **[technologies] maps**

# A map displays outdoor or indoor geographical data in your app or on your website.

![https://developer.apple.com/design/human-interface-guidelines/images/intro/technologies/technology-maps-intro_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/technologies/technology-maps-intro_2x.png)

A map uses a familiar interface that supports much of the same functionality as the system-provided Maps app, such as zooming, panning, and rotation. A map can also include annotations and overlays and show routing information, and you can configure it to use a standard graphical view, a satellite imagery-based view, or a view that’s a hybrid of both.

# **Best practices**

**In general, make your map interactive.** People expect to be able to zoom, pan, and otherwise interact with maps in familiar ways. Noninteractive elements, such as overlays that obscure the map, can interfere with people’s expectations for how maps behave.

**Pick a map emphasis style that suits the needs of your app.** There are two emphasis styles to choose from:

- The *default* style presents a version of the map with fully saturated colors, and is a good option for most standard map applications without a lot of custom elements. This style is also useful for keeping visual alignment between your map and the Maps app, in situations when people might switch between them.
- The *muted* style, by contrast, presents a desaturated version of the map. This style is great if you have a lot of information-rich content that you want to stand out against the map.

See [Custom information](https://developer.apple.com/design/human-interface-guidelines/technologies/maps#custom-information) for additional guidance.

**Help people find your app’s content.** Consider offering a search feature combined with a way to filter locations by category. The search field for a shopping mall map, for example, might include filters that make it easy to find common store types, like clothing, housewares, electronics, jewelry, and toys.

**Clearly identify elements that people select.** When someone selects a specific area or other element on the map, use distinct styling like an outline and color variation to call attention to the selection.

**Cluster overlapping points of interest to improve map legibility.** A *cluster* uses a single pin to represent multiple points of interest within close proximity. As people zoom in on a map, clusters expand to progressively reveal individual points of interest.

**Help people see the Apple logo and legal link.** It's fine when parts of your interface temporarily cover the logo and link, but don't cover these elements all the time. To help you maintain the visibility of the Apple logo and legal link, follow these recommendations.

- Use adequate padding to separate the logo and link from the map boundaries and your custom controls. For example, it works well to use 7 points of padding on the sides of the elements and 10 points above and below them.
- Avoid causing the logo and link to move with your interface. It's best when the Apple logo and legal link appear to be fixed to the map.
- If your custom interface can move relative to the map, use the lowest position of the custom element to determine the placement of the logo and link. For example, if your app lets people pull up a custom card from the bottom of the screen, place the Apple logo and legal link 10 points above the lowest resting position of the card.

**NOTE**The Apple logo and legal link aren't shown on maps that are smaller than 200x100 pixels.

# **Custom information**

**Use annotations that match the visual style of your app.** Annotations identify custom points of interest on your map. The default annotation marker has a red tint and a white pin icon. You can change the tint to match the color scheme of your app. You can also change the icon to a string or image, like a logo. An icon string can contain any characters, including Unicode characters, but keep it to two to three characters in length for readability. For developer guidance, see [MKAnnotationView](https://developer.apple.com/documentation/mapkit/mkannotationview).

**If you want to display custom information that’s related to standard map features, consider making them independently selectable.** When you enable selectable map features, the system treats Apple-provided features (including points of interest, territories, and physical features) independently from other annotations that you add. You can configure custom appearances and information to represent these features when people select them. For developer guidance, see [MKMapFeatureOptions](https://developer.apple.com/documentation/mapkit/mkmapfeatureoptions).

**Use overlays to define map areas with a specific relationship to your content.**

- *Above roads*, the default level, places the overlay above roads but below buildings, trees, and other features. This is great for situations where you want people to have an idea of what’s below the overlay, while still clearly understanding that it’s a defined space.
- *Above labels* places the overlay above both roads and labels, hiding everything beneath it. This is useful for content that you want to be fully abstracted from the features of the map, or when you want to hide areas of the map that aren’t relevant.

**Make sure there’s enough contrast between custom controls and the map.** Insufficient contrast makes controls hard to see and can cause them to blend in with the map. Consider using a thin stroke or light drop shadow to help a custom control stand out, or applying blend modes to the map area to increase its contrast with the controls atop it.

# **Indoor maps**

Apps connected with specific venues like shopping malls and stadiums can design custom interactive maps that help people locate and navigate to indoor points of interest. Indoor maps can include overlays that highlight specific areas, such as rooms, kiosks, and other locations. They can also include text labels, icons, and routes.

• [Example 1](https://developer.apple.com/design/human-interface-guidelines/technologies/maps#)
• [Example 2](https://developer.apple.com/design/human-interface-guidelines/technologies/maps#)
• [Example 3](https://developer.apple.com/design/human-interface-guidelines/technologies/maps#)

-

![https://developer.apple.com/design/human-interface-guidelines/technologies/maps/images/maps_indoor1_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/maps/images/maps_indoor1_2x.png)


**Adjust map detail based on the zoom level.** Too much detail can cause a map to appear cluttered. Show large areas like rooms and buildings at all zoom levels. Then, progressively add more detailed features and labels as the map is zoomed in. An airport map might show only terminals and gates when zoomed out, but reveal individual stores and restrooms when zoomed in.

![https://developer.apple.com/design/human-interface-guidelines/technologies/maps/images/maps_indoor4_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/maps/images/maps_indoor4_2x.png)

**Use distinctive styling to differentiate the features of your map.** Using color along with iconography can help distinguish different types of areas, stores, and services, and make it easy for people to quickly find what they're looking for.

**Offer a floor picker if your venue includes multiple levels.** A floor picker lets people quickly jump between floors. If you implement this feature, keep floor numbers concise for simplicity. In most cases, a list of floor numbers — rather than floor names — is sufficient.

![https://developer.apple.com/design/human-interface-guidelines/technologies/maps/images/maps_indoor5_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/maps/images/maps_indoor5_2x.png)

**Include surrounding areas to provide context.** Adjacent streets, playgrounds, and other nearby locations can all help orient people when they use your map. If these areas are noninteractive, use dimming and a distinct color to make them appear supplemental.

**Consider enabling navigation between your venue and nearby transit points.** Make it easy to enter and exit your venue by offering routing to and from nearby bus stops, train stations, parking lots, garages, and other transit locations. You might also offer a way for people to quickly switch over to Apple Maps for additional navigation options.

**Limit scrolling outside of your venue.** This can help people avoid getting lost when they swipe too hard on your map. When possible, keep at least part of your indoor map visible onscreen at all times. To help people stay oriented, you may need to adjust the amount of scrolling you permit based on the zoom level.

**Design an indoor map that feels like a natural extension of your app.** Don’t try to replicate the appearance of Apple Maps. Instead, make sure area overlays, icons, and text match the visual style of your app.

You use a specific, distinct format to create indoor maps; to learn more, see [Indoor Mapping Data Format](https://register.apple.com/resources/imdf/).

# **Platform considerations**

*No additional considerations for iOS, iPadOS, macOS, or tvOS.*

# **watchOS**

On Apple Watch, maps are static snapshots of geographic locations. Place a map in your interface at design time and show the appropriate region at runtime. The displayed region isn't interactive; tapping it opens the Maps app on Apple Watch. You can annotate the map to highlight points of interest or other relevant information. The system lets you add up to five annotations to a map.

![https://developer.apple.com/design/human-interface-guidelines/technologies/maps/images/maps_watch1_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/maps/images/maps_watch1_2x.png)

**Fit the map interface element to the screen.** The entire element should be visible on the Apple Watch display without requiring scrolling.

**Show the smallest region that encompasses the points of interest.** The content within a map interface element doesn't scroll, so all key content must be visible within the displayed region.

For developer guidance, see [WKInterfaceMap](https://developer.apple.com/documentation/watchkit/wkinterfacemap).