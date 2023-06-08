# **[technologies] maps**

# A map displays outdoor or indoor geographical data in your app or on your website.
> 지도는 앱 또는 웹 사이트에 실외 또는 실내 지리적 데이터를 표시합니다.
>




![https://developer.apple.com/design/human-interface-guidelines/images/intro/technologies/technology-maps-intro_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/technologies/technology-maps-intro_2x.png)

A map uses a familiar interface that supports much of the same functionality as the system-provided Maps app, such as zooming, panning, and rotation. A map can also include annotations and overlays and show routing information, and you can configure it to use a standard graphical view, a satellite imagery-based view, or a view that’s a hybrid of both.
> 지도는 확대/축소, 이동 및 회전과 같은 시스템에서 제공하는 지도 앱과 동일한 기능을 지원하는 친숙한 인터페이스를 사용합니다. 지도에는 주석과 오버레이가 포함되어 라우팅 정보를 표시할 수도 있으며 표준 그래픽 보기, 위성 이미지 기반 보기 또는 둘을 혼합한 보기를 사용하도록 지도를 구성할 수 있습니다.
>




# **Best practices**

**In general, make your map interactive.** People expect to be able to zoom, pan, and otherwise interact with maps in familiar ways. Noninteractive elements, such as overlays that obscure the map, can interfere with people’s expectations for how maps behave.
> 일반적으로 지도를 상호작용적으로 만드십시오. 사람들은 지도를 확대하거나 이동하거나 다른 방법으로 친숙한 방식으로 지도와 상호작용할 수 있기를 기대합니다. 지도를 흐리게 하는 오버레이와 같은 대화형이 아닌 요소는 지도가 작동하는 방식에 대한 사람들의 기대를 방해할 수 있다.
>




**Pick a map emphasis style that suits the needs of your app.** There are two emphasis styles to choose from:
> 앱의 요구 사항에 맞는 지도 강조 스타일을 선택하십시오. 두 가지 강조 스타일 중에서 선택할 수 있습니다:
>




- The *default* style presents a version of the map with fully saturated colors, and is a good option for most standard map applications without a lot of custom elements. This style is also useful for keeping visual alignment between your map and the Maps app, in situations when people might switch between them.
- >  기본 스타일은 완전히 포화된 색상으로 지도 버전을 표시하며, 많은 사용자 지정 요소가 없는 대부분의 표준 지도 응용 프로그램에 적합한 옵션입니다. 이 스타일은 사람들이 지도와 지도 앱을 전환할 수 있는 상황에서 지도와 지도 앱 간의 시각적 정렬을 유지하는 데도 유용합니다.

- The *muted* style, by contrast, presents a desaturated version of the map. This style is great if you have a lot of information-rich content that you want to stand out against the map.
- >  대조적으로, 음소거된 스타일은 지도의 불포화 버전을 나타낸다. 이 스타일은 정보가 풍부한 콘텐츠가 많아 지도와 대조하여 돋보이고 싶은 경우에 적합합니다.


See [Custom information](https://developer.apple.com/design/human-interface-guidelines/technologies/maps#custom-information) for additional guidance.

**Help people find your app’s content.** Consider offering a search feature combined with a way to filter locations by category. The search field for a shopping mall map, for example, might include filters that make it easy to find common store types, like clothing, housewares, electronics, jewelry, and toys.
> 사용자가 앱의 콘텐츠를 찾을 수 있도록 도와줍니다. 카테고리별로 위치를 필터링하는 방법과 함께 검색 기능을 제공하는 것을 고려해 보십시오. 예를 들어, 쇼핑몰 맵의 검색 필드에는 의류, 가정용품, 전자제품, 보석 및 장난감과 같은 일반적인 상점 유형을 쉽게 찾을 수 있는 필터가 포함될 수 있습니다.
>




**Clearly identify elements that people select.** When someone selects a specific area or other element on the map, use distinct styling like an outline and color variation to call attention to the selection.
> 사람들이 선택하는 요소를 명확하게 식별합니다. 누군가가 지도에서 특정 영역이나 다른 요소를 선택할 때, 선택에 주의를 환기하기 위해 윤곽선과 색상 변화와 같은 뚜렷한 스타일을 사용하십시오.
>




**Cluster overlapping points of interest to improve map legibility.** A *cluster* uses a single pin to represent multiple points of interest within close proximity. As people zoom in on a map, clusters expand to progressively reveal individual points of interest.
> 관심 지점을 겹쳐서 클러스터하여 지도를 읽을 수 있도록 합니다. 클러스터는 단일 핀을 사용하여 근접하게 여러 관심 지점을 나타냅니다. 사람들이 지도를 확대하면 클러스터가 확장되어 개별 관심 지점이 점진적으로 표시됩니다.
>




**Help people see the Apple logo and legal link.** It's fine when parts of your interface temporarily cover the logo and link, but don't cover these elements all the time. To help you maintain the visibility of the Apple logo and legal link, follow these recommendations.
> 사용자가 Apple 로고와 법적 링크를 볼 수 있도록 도와줍니다. 인터페이스의 일부가 일시적으로 로고와 링크를 가리더라도 좋지만 이러한 요소를 항상 가리지는 마십시오. Apple 로고 및 법적 링크의 가시성을 유지하려면 다음 권장 사항을 따르십시오.
>




- Use adequate padding to separate the logo and link from the map boundaries and your custom controls. For example, it works well to use 7 points of padding on the sides of the elements and 10 points above and below them.
- >  적절한 패딩을 사용하여 지도 경계 및 사용자 정의 컨트롤에서 로고 및 링크를 분리합니다. 예를 들어, 요소의 측면에 7개의 패딩 포인트를 사용하고 그 위와 아래에 10개의 패딩 포인트를 사용하는 것이 좋습니다.

- Avoid causing the logo and link to move with your interface. It's best when the Apple logo and legal link appear to be fixed to the map.
- >  로고와 링크가 인터페이스와 함께 이동하지 않도록 합니다. Apple 로고와 법적 링크가 지도에 고정된 것처럼 보일 때가 가장 좋습니다.

- If your custom interface can move relative to the map, use the lowest position of the custom element to determine the placement of the logo and link. For example, if your app lets people pull up a custom card from the bottom of the screen, place the Apple logo and legal link 10 points above the lowest resting position of the card.
- >  사용자 지정 인터페이스가 지도를 기준으로 이동할 수 있는 경우 사용자 지정 요소의 가장 낮은 위치를 사용하여 로고와 링크의 위치를 결정합니다. 예를 들어, 앱에서 사용자 지정 카드를 화면 아래에서 끌어 올릴 수 있는 경우, Apple 로고와 법적 링크를 카드의 가장 낮은 정지 위치보다 10포인트 위에 놓습니다.


**NOTE**The Apple logo and legal link aren't shown on maps that are smaller than 200x100 pixels.
> 참고: Apple 로고와 법적 링크는 200x100픽셀보다 작은 지도에는 표시되지 않습니다.
>




# **Custom information**

**Use annotations that match the visual style of your app.** Annotations identify custom points of interest on your map. The default annotation marker has a red tint and a white pin icon. You can change the tint to match the color scheme of your app. You can also change the icon to a string or image, like a logo. An icon string can contain any characters, including Unicode characters, but keep it to two to three characters in length for readability. For developer guidance, see [MKAnnotationView](https://developer.apple.com/documentation/mapkit/mkannotationview).
> 앱의 시각적 스타일과 일치하는 주석을 사용하십시오. 주석은 지도에서 사용자 지정 관심 지점을 식별합니다. 기본 주석 마커에는 빨간색 색조와 흰색 핀 아이콘이 있습니다. 앱의 색 구성표에 맞게 색을 변경할 수 있습니다. 아이콘을 로고와 같은 문자열이나 이미지로 변경할 수도 있습니다. 아이콘 문자열은 유니코드 문자를 포함한 모든 문자를 포함할 수 있지만 읽기 쉽도록 2~3자로 유지됩니다. 개발자 지침은 MK 주석 보기를 참조하십시오.
>




**If you want to display custom information that’s related to standard map features, consider making them independently selectable.** When you enable selectable map features, the system treats Apple-provided features (including points of interest, territories, and physical features) independently from other annotations that you add. You can configure custom appearances and information to represent these features when people select them. For developer guidance, see [MKMapFeatureOptions](https://developer.apple.com/documentation/mapkit/mkmapfeatureoptions).
> 표준 지도 기능과 관련된 사용자 지정 정보를 표시하려면 지도 기능을 독립적으로 선택할 수 있도록 설정하는 것이 좋습니다. 선택 가능한 지도 기능을 사용하도록 설정하면 시스템은 사용자가 추가하는 다른 주석과 독립적으로 Apple에서 제공하는 기능(관심 지점, 영역 및 물리적 기능 포함)을 처리합니다. 사용자가 이러한 기능을 선택할 때 이러한 기능을 나타내도록 사용자 정의 모양 및 정보를 구성할 수 있습니다. 개발자 지침은 MKMap 기능 옵션을 참조하십시오.
>




**Use overlays to define map areas with a specific relationship to your content.**
> 오버레이를 사용하여 내용과 특정 관계가 있는 지도 영역을 정의합니다.
>




- *Above roads*, the default level, places the overlay above roads but below buildings, trees, and other features. This is great for situations where you want people to have an idea of what’s below the overlay, while still clearly understanding that it’s a defined space.
- >  기본 수준인 도로 위에서는 도로 위에 오버레이를 배치하지만 건물, 나무 및 기타 피쳐 아래에는 오버레이를 배치합니다. 이것은 사람들이 정의된 공간이라는 것을 명확하게 이해하면서 오버레이 아래에 무엇이 있는지에 대한 아이디어를 얻기를 원하는 상황에 매우 유용합니다.

- *Above labels* places the overlay above both roads and labels, hiding everything beneath it. This is useful for content that you want to be fully abstracted from the features of the map, or when you want to hide areas of the map that aren’t relevant.
- >  위의 레이블은 오버레이를 도로와 레이블 위에 배치하고 그 아래의 모든 것을 숨깁니다. 이 기능은 지도의 기능에서 완전히 추상화하려는 내용이나 관련이 없는 지도 영역을 숨기려는 경우에 유용합니다.


**Make sure there’s enough contrast between custom controls and the map.** Insufficient contrast makes controls hard to see and can cause them to blend in with the map. Consider using a thin stroke or light drop shadow to help a custom control stand out, or applying blend modes to the map area to increase its contrast with the controls atop it.
> 사용자 지정 컨트롤과 맵 사이에 충분한 대비가 있는지 확인하십시오. 대비가 부족하면 컨트롤이 잘 보이지 않고 맵과 혼합될 수 있습니다. 사용자 정의 컨트롤이 눈에 잘 띄도록 얇은 스트로크 또는 밝은 드롭 섀도를 사용하거나 지도 영역에 혼합 모드를 적용하여 위의 컨트롤과 대비를 높이는 것을 고려하십시오.
>




# **Indoor maps**

Apps connected with specific venues like shopping malls and stadiums can design custom interactive maps that help people locate and navigate to indoor points of interest. Indoor maps can include overlays that highlight specific areas, such as rooms, kiosks, and other locations. They can also include text labels, icons, and routes.
> 쇼핑몰이나 경기장과 같은 특정 장소와 연결된 앱은 사람들이 실내의 관심 지점을 찾고 탐색하는 것을 돕는 맞춤형 대화형 지도를 설계할 수 있다. 실내 지도에는 룸, 키오스크 및 기타 위치와 같은 특정 영역을 강조 표시하는 오버레이가 포함될 수 있습니다. 텍스트 레이블, 아이콘 및 경로도 포함할 수 있습니다.
>




• [Example 1](../technologies/maps#)
• [Example 2](../technologies/maps#)
• [Example 3](../technologies/maps#)

-

![https://developer.apple.com/design/human-interface-guidelines/technologies/maps/images/maps_indoor1_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/maps/images/maps_indoor1_2x.png)


**Adjust map detail based on the zoom level.** Too much detail can cause a map to appear cluttered. Show large areas like rooms and buildings at all zoom levels. Then, progressively add more detailed features and labels as the map is zoomed in. An airport map might show only terminals and gates when zoomed out, but reveal individual stores and restrooms when zoomed in.
> 확대/축소 수준에 따라 지도 세부 정보를 조정합니다. 세부 정보가 너무 많으면 지도가 흐트러질 수 있습니다. 모든 확대/축소 수준에서 회의실 및 건물과 같은 넓은 영역을 표시합니다. 그런 다음 지도가 확대됨에 따라 점진적으로 더 자세한 기능과 레이블을 추가합니다. 공항 지도는 축소할 때 터미널과 게이트만 표시할 수 있지만 확대할 때는 개별 상점과 화장실이 표시됩니다.
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/maps/images/maps_indoor4_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/maps/images/maps_indoor4_2x.png)

**Use distinctive styling to differentiate the features of your map.** Using color along with iconography can help distinguish different types of areas, stores, and services, and make it easy for people to quickly find what they're looking for.
> 독특한 스타일을 사용하여 지도의 특징을 구별할 수 있습니다. 아이콘과 함께 색상을 사용하면 지역, 상점 및 서비스의 다양한 유형을 구분하는 데 도움이 되고 사람들이 원하는 것을 쉽게 찾을 수 있습니다.
>




**Offer a floor picker if your venue includes multiple levels.** A floor picker lets people quickly jump between floors. If you implement this feature, keep floor numbers concise for simplicity. In most cases, a list of floor numbers — rather than floor names — is sufficient.
> 장소에 여러 층이 있는 경우 바닥 피커를 제공합니다. 바닥 피커를 사용하면 사람들이 층 사이를 빠르게 이동할 수 있습니다. 이 기능을 구현할 경우 단순성을 위해 층 번호를 간결하게 유지하십시오. 대부분의 경우 플로어 이름보다는 플로어 번호 목록으로 충분합니다.
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/maps/images/maps_indoor5_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/maps/images/maps_indoor5_2x.png)

**Include surrounding areas to provide context.** Adjacent streets, playgrounds, and other nearby locations can all help orient people when they use your map. If these areas are noninteractive, use dimming and a distinct color to make them appear supplemental.
> 주변 지역을 포함하여 상황에 맞는 거리, 놀이터 및 기타 가까운 위치는 모두 사용자가 지도를 사용할 때 사용자의 방향을 지정하는 데 도움이 있습니다. 이러한 영역이 상호 작용하지 않는 경우 조광 및 뚜렷한 색상을 사용하여 보충적으로 표시합니다.
>




**Consider enabling navigation between your venue and nearby transit points.** Make it easy to enter and exit your venue by offering routing to and from nearby bus stops, train stations, parking lots, garages, and other transit locations. You might also offer a way for people to quickly switch over to Apple Maps for additional navigation options.
> 행사장과 가까운 환승 지점 사이를 탐색할 수 있도록 하십시오. 가까운 버스 정류장, 기차역, 주차장, 차고 및 기타 환승 위치로 이동하는 경로를 제공하여 행사장을 쉽게 출입할 수 있습니다. 또한 사용자가 Apple Maps로 빠르게 전환하여 추가 탐색 옵션을 얻을 수 있는 방법을 제공할 수도 있습니다.
>




**Limit scrolling outside of your venue.** This can help people avoid getting lost when they swipe too hard on your map. When possible, keep at least part of your indoor map visible onscreen at all times. To help people stay oriented, you may need to adjust the amount of scrolling you permit based on the zoom level.
> 행사장 밖으로 스크롤하는 것을 제한합니다. 이렇게 하면 사람들이 지도를 너무 세게 밀었을 때 길을 잃는 것을 방지할 수 있습니다. 가능한 경우 실내 지도의 적어도 일부를 항상 화면에 표시하도록 합니다. 사용자가 방향을 유지할 수 있도록 하려면 확대/축소 수준에 따라 허용되는 스크롤 양을 조정해야 할 수 있습니다.
>




**Design an indoor map that feels like a natural extension of your app.** Don’t try to replicate the appearance of Apple Maps. Instead, make sure area overlays, icons, and text match the visual style of your app.
> 앱의 자연스러운 확장처럼 느껴지는 실내 지도를 디자인하십시오. Apple Maps의 모양을 복제하려고 하지 마십시오. 대신 영역 오버레이, 아이콘 및 텍스트가 앱의 시각적 스타일과 일치하는지 확인하십시오.
>




You use a specific, distinct format to create indoor maps; to learn more, see [Indoor Mapping Data Format](https://register.apple.com/resources/imdf/).
> 고유한 형식을 사용하여 실내 지도를 만들 수 있습니다. 자세한 내용은 실내 매핑 데이터 형식을 참조하십시오.
>




# **Platform considerations**

*No additional considerations for iOS, iPadOS, macOS, or tvOS.*
> iOS, iPadOS, macOS 또는 tvOS에 대한 추가 고려 사항은 없습니다.
>




# **watchOS**

On Apple Watch, maps are static snapshots of geographic locations. Place a map in your interface at design time and show the appropriate region at runtime. The displayed region isn't interactive; tapping it opens the Maps app on Apple Watch. You can annotate the map to highlight points of interest or other relevant information. The system lets you add up to five annotations to a map.
> Apple Watch에서 지도는 지리적 위치의 정적 스냅샷입니다. 설계 시 인터페이스에 지도를 배치하고 실행 시 적절한 영역을 표시합니다. 표시된 영역은 대화형이 아닙니다. 이 영역을 누르면 Apple Watch에서 지도 앱이 열립니다. 지도에 주석을 달아 관심 지점이나 기타 관련 정보를 강조 표시할 수 있습니다. 이 시스템을 사용하면 지도에 최대 5개의 주석을 추가할 수 있습니다.
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/maps/images/maps_watch1_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/maps/images/maps_watch1_2x.png)

**Fit the map interface element to the screen.** The entire element should be visible on the Apple Watch display without requiring scrolling.
> 지도 인터페이스 요소를 화면에 맞춥니다. 스크롤할 필요 없이 전체 요소가 Apple Watch 디스플레이에 표시되어야 합니다.
>




**Show the smallest region that encompasses the points of interest.** The content within a map interface element doesn't scroll, so all key content must be visible within the displayed region.
> 관심 지점을 포함하는 가장 작은 영역을 표시합니다. 지도 인터페이스 요소 내의 콘텐츠는 스크롤되지 않으므로 표시된 영역 내에서 모든 주요 콘텐츠를 볼 수 있어야 합니다.
>




For developer guidance, see [WKInterfaceMap](https://developer.apple.com/documentation/watchkit/wkinterfacemap).
