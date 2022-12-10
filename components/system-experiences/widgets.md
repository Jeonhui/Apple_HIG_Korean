# **[components-status] widgets**

## A widget elevates a small amount of timely, personally relevant information from your app or game, displaying it where people can see it at a glance.
> 위젯은 앱이나 게임에서 개인적으로 관련된 소량의 정보를 적시에 끌어올려 사람들이 한 눈에 볼 수 있는 위치에 표시합니다.
>




![https://developer.apple.com/design/human-interface-guidelines/images/intro/components/widgets-intro-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/components/widgets-intro-dark_2x.png)

Widgets display app content without requiring people to open your app. Useful and delightful, widgets can also help people make their devices more personal. For developer guidance, see [Creating a widget extension](https://developer.apple.com/documentation/widgetkit/creating-a-widget-extension).
> 위젯은 사용자가 앱을 열지 않아도 앱 콘텐츠를 표시합니다. 유용하고 즐거운 위젯은 또한 사람들이 기기를 더 개인적으로 만들 수 있도록 도와줍니다. 개발자 지침은 위젯 확장자 만들기를 참조하십시오.
>




In iOS and iPadOS, widgets appear on the Home Screen or in Today View; in macOS, Notification Center displays widgets. Widgets can be small, medium, large, and — in iPadOS only — extra large.
> iOS 및 iPadOS에서는 위젯이 홈 화면 또는 오늘 보기에 표시되고, macOS에서는 Notification Center가 위젯을 표시합니다. 위젯은 소형, 중형, 대형 및 iPad에서 사용할 수 있습니다.OS만 해당 — 특대형.
>




iOS 16 introduces widgets on the Lock Screen, which let people place rich, glanceable content on their iPhone Lock Screen in a way that’s similar to placing a complication on their Apple Watch face. Lock Screen widgets are also similar to complications in both design and implementation. For guidance, see [Platform considerations](https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/widgets#platform-considerations) below.
> iOS 16은 잠금 화면에 위젯을 도입하여 사람들이 아이폰 잠금 화면에 풍부하고 눈에 띄는 콘텐츠를 애플 워치의 얼굴에 복잡하게 배치하는 것과 유사한 방식으로 배치할 수 있도록 한다. 잠금 화면 위젯은 또한 설계와 구현 모두에서 복잡성과 유사합니다. 자세한 내용은 아래 플랫폼 고려사항을 참조하십시오.
>




The widget gallery helps people find the widgets they want in the sizes that work for them. The gallery’s editing mode lets people make changes to editable widgets, such as changing the location in a Weather widget or selecting a topic in a News widget. The widget gallery is available in Today View and Home Screen editing mode in iOS and iPadOS. It’s also available in Lock Screen editing mode in iOS and in Notification Center editing mode in macOS.
> 위젯 갤러리는 사용자가 원하는 크기의 위젯을 찾을 수 있도록 도와줍니다. 갤러리의 편집 모드를 사용하면 날씨 위젯에서 위치를 변경하거나 뉴스 위젯에서 주제를 선택하는 등 편집 가능한 위젯을 변경할 수 있습니다. 위젯 갤러리는 iOS 및 iPadOS에서 오늘 보기 및 홈 화면 편집 모드로 사용할 수 있습니다. iOS에서는 잠금 화면 편집 모드, MacOS에서는 알림 센터 편집 모드에서도 사용할 수 있습니다.
>




In iOS and iPadOS, the widget gallery also supports widget stacks, including a Smart Stack. A stack contains up to 10 same-size widgets; people view one widget at a time by scrolling through the stack. A Smart Stack automatically rotates through the stack of widgets, displaying the widget most likely to be relevant in the current context. Smart Stacks aren't available on the Lock Screen on iPhone and iPad.
> iOS와 아이패드 OS에서 위젯 갤러리는 스마트 스택을 포함한 위젯 스택도 지원합니다. 스택은 최대 10개의 동일한 크기의 위젯을 포함하며, 사용자는 스택을 스크롤하여 한 번에 하나의 위젯을 봅니다. 스마트 스택은 위젯 스택을 통해 자동으로 회전하여 현재 컨텍스트와 가장 관련성이 높은 위젯을 표시합니다. 스마트 스택은 iPhone과 iPad의 잠금 화면에서 사용할 수 없습니다.
>




Siri can add a suggested widget to the Smart Stack when it’s likely that people are interested in it. A suggested widget doesn’t stay in the Smart Stack unless people choose to keep it. For developer guidance, see [Increasing the visibility of widgets in Smart Stacks](https://developer.apple.com/documentation/widgetkit/widget-suggestions-in-smart-stacks).
> Siri는 사람들이 스마트 스택에 관심을 가질 가능성이 있을 때 제안된 위젯을 추가할 수 있습니다. 제안된 위젯은 사용자가 유지하도록 선택하지 않는 한 스마트 스택에 유지되지 않습니다. 개발자 지침은 스마트 스택에서 위젯 가시성 향상을 참조하십시오.
>




# **Best practices**

The first step in the design process is to choose a single idea for your widget. Throughout the process, use that idea to keep the widget’s content focused and relevant.
> 설계 프로세스의 첫 번째 단계는 위젯에 대한 단일 아이디어를 선택하는 것입니다. 프로세스 전반에 걸쳐 이 아이디어를 사용하여 위젯의 콘텐츠에 초점을 맞추고 관련성을 유지합니다.
>




**Look for a simple idea that’s clearly related to your app’s main purpose.** For example, the widget for Weather shows current high and low temperatures plus the current weather conditions. This is the information most people who use the Weather app are primarily interested in. Alternatively, another weather app might offer people the ability to see other types of weather data such as pressure, humidity, or wind speed.
> 예를 들어 날씨 위젯에서는 현재 고온 및 저온과 현재 날씨 상태를 보여 줍니다. 이것은 날씨 앱을 사용하는 대부분의 사람들이 주로 관심을 갖는 정보입니다. 또는 다른 날씨 앱은 사람들에게 압력, 습도 또는 풍속과 같은 다른 유형의 날씨 데이터를 볼 수 있는 능력을 제공할 수 있다.
>




![https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/widgets/images/focused-widget_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/widgets/images/focused-widget_2x.png)

**In each size, display only the information that’s directly related to the widget’s main purpose.** In larger widgets, you can display more data — or more detailed visualizations of the data — but it’s crucial to stay focused on the widget’s purpose. For example, all Calendar widgets display a person’s upcoming events. In each size from small to extra large, the widget maintains its focus on events while expanding the range of information as the size increases.
> 각 크기에는 위젯의 주요 목적과 직접 관련된 정보만 표시합니다. 큰 위젯에서는 더 많은 데이터 또는 데이터의 더 자세한 시각화를 표시할 수 있지만 위젯의 목적에 집중하는 것이 중요합니다. 예를 들어, 모든 일정관리 위젯은 사용자의 예정된 이벤트를 표시합니다. 작은 것부터 큰 것까지 각각의 크기에서 위젯은 이벤트에 대한 초점을 유지하면서 크기가 증가함에 따라 정보의 범위를 확장합니다.
>




• [Small](../components/system-experiences/widgets#)
• [Medium](../components/system-experiences/widgets#)
• [Large](../components/system-experiences/widgets#)
• [Extra Large (iPad only)](../components/system-experiences/widgets#)

-

![https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/widgets/images/calendar-small_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/widgets/images/calendar-small_2x.png)


**Avoid creating a widget that only launches your app.** People appreciate widgets because they provide instant access to meaningful content. A widget that behaves like an app icon offers no additional value, which means people are likely to remove it from their screens.
> 앱만 시작하는 위젯을 만들지 마십시오. 위젯은 의미 있는 콘텐츠에 즉시 액세스할 수 있기 때문에 사람들이 위젯을 높이 평가합니다. 앱 아이콘처럼 행동하는 위젯은 추가적인 가치를 제공하지 않으며, 이는 사람들이 화면에서 위젯을 제거할 가능성이 높다는 것을 의미합니다.
>




**Offer your widget in multiple sizes when doing so adds value.** In general, avoid simply expanding a smaller widget’s content to fill a larger area. It’s more important to create one widget in the size that works best for the content you want to display than it is to provide the widget in all sizes.
> 위젯을 여러 크기로 제공하여 가치를 높입니다. 일반적으로 작은 위젯의 내용을 단순히 확장하여 더 큰 영역을 채우지 마십시오. 모든 크기의 위젯을 제공하는 것보다 표시할 내용에 가장 적합한 크기의 위젯을 하나 만드는 것이 더 중요합니다.
>




**Prefer dynamic information that changes throughout the day.** If a widget’s content never appears to change, people may not keep it in a prominent position. Although widgets don’t update from minute to minute, it’s important to find ways to keep their content fresh to invite frequent viewing.
> 하루 종일 변화하는 동적 정보를 선호합니다. 위젯의 내용이 절대 변하지 않는 것처럼 보일 경우 사람들이 눈에 띄는 위치에 유지하지 못할 수 있습니다. 위젯이 시시각각 업데이트되지는 않지만 자주 볼 수 있도록 내용을 새로 유지하는 방법을 찾는 것이 중요합니다.
>




**Look for opportunities to surprise and delight.** For example, you might design a unique visual treatment for your calendar widget to display on meaningful occasions, like birthdays or holidays.
> 예를 들어, 생일이나 공휴일과 같은 의미 있는 경우에 달력 위젯이 표시할 수 있는 고유한 시각적 처리를 설계할 수 있습니다.
>




![https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/widgets/images/surprise-and-delight_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/widgets/images/surprise-and-delight_2x.png)

# **Updating widget content**

To remain relevant and useful, widgets periodically refresh their information. Widgets don’t support continuous, real-time updates, and the system may adjust the limits for updates depending on various factors.
> 관련성과 유용성을 유지하기 위해 위젯은 주기적으로 정보를 새로 고칩니다. 위젯은 지속적인 실시간 업데이트를 지원하지 않으며, 시스템은 다양한 요인에 따라 업데이트 제한을 조정할 수 있습니다.
>




**Keep your widget up to date.** Finding the appropriate update frequency for your widget depends on knowing how often the data changes and estimating how often people need to see new data. For example, a widget that helps people track tides at a beach could provide useful information on an hourly basis, even though tide conditions change constantly. If people are likely to check your widget more frequently than you can update it, consider displaying text that describes when the data was last updated. For developer guidance, see [Keeping a widget up to date](https://developer.apple.com/documentation/widgetkit/keeping-a-widget-up-to-date).
> 위젯을 최신 상태로 유지합니다. 위젯에 적합한 업데이트 빈도를 찾는 방법은 데이터가 변경되는 빈도를 알고 사용자가 새 데이터를 보는 빈도를 추정하는 방법에 따라 달라집니다. 예를 들어, 사람들이 해변에서 조수를 추적하는 것을 돕는 위젯은 조수의 조건이 끊임없이 변화하더라도 시간 단위로 유용한 정보를 제공할 수 있다. 사용자가 업데이트할 수 있는 것보다 더 자주 위젯을 확인하는 경우 데이터가 마지막으로 업데이트된 시간을 설명하는 텍스트를 표시하는 것이 좋습니다. 개발자 지침은 위젯을 최신 상태로 유지를 참조하십시오.
>




**Let the system update dates and times in your widget.** Widget update frequency is limited, and you can preserve some of your update opportunities by letting the system refresh date and time information.
> 위젯의 날짜 및 시간을 시스템에서 업데이트하도록 합니다. 위젯 업데이트 빈도는 제한적이며, 시스템에서 날짜 및 시간 정보를 새로 고치도록 하여 일부 업데이트 기회를 보존할 수 있습니다.
>




**Show content quickly.** When you determine the update frequency that fits with the data you display, you don’t need to hide stale data behind placeholder content.
> 내용을 빨리 표시합니다. 표시하는 데이터에 맞는 업데이트 빈도를 결정할 때 오래된 데이터를 자리 표시자 내용 뒤에 숨길 필요가 없습니다.
>




# **Interactivity**

In some cases, people need to edit a widget to ensure it displays the information that’s most useful for them. For example, people choose a stock symbol for a Stocks Symbol widget. In contrast, some widgets — like the Podcasts widget — automatically display recent content, so people don’t need to customize them.
> 경우에 따라 사용자는 위젯을 편집하여 가장 유용한 정보를 표시해야 합니다. 예를 들어, 사람들은 주식 기호 위젯에 대한 주식 기호를 선택합니다. 대조적으로 팟캐스트 위젯과 같은 일부 위젯은 최근 내용을 자동으로 표시하므로 사용자가 사용자 정의할 필요가 없습니다.
>




**Make editable widgets easy for people to customize.** If your widget is editable, avoid requiring too many settings or asking for information that might be hard for people to find. You don’t have to design an editing-mode user interface for your widget because the system automatically generates it for you. For developer guidance, see [Making a configurable widget](https://developer.apple.com/documentation/widgetkit/making-a-configurable-widget).
> 편집 가능한 위젯을 사용자가 쉽게 사용자 지정할 수 있도록 합니다. 위젯을 편집할 수 있는 경우 너무 많은 설정을 요구하거나 사용자가 찾기 어려운 정보를 요청하지 않도록 합니다. 위젯이 자동으로 생성되므로 위젯에 대한 편집 모드 사용자 인터페이스를 설계할 필요가 없습니다. 개발자 지침은 구성 가능한 위젯 만들기를 참조하십시오.
>




**Ensure that a widget interaction opens your app at the right location.**When people interact with your widget, it deep links into your app, where you can offer details and actions that directly relate to the widget’s content. Avoid making people navigate to the relevant area. For example, when people click or tap a Stocks Symbol widget, the Stocks app opens to a page that displays information about that symbol. Similarly, when people click or tap a small Stocks Watchlist widget, the app opens to show the complete watchlist. When people click or tap one symbol in a larger version of the Watchlist widget, Stocks open to show that symbol.
> 위젯 상호 작용을 통해 올바른 위치에서 앱이 열리는지 확인합니다.사용자가 위젯과 상호 작용하면 앱에 깊이 연결되어 위젯의 내용과 직접 관련된 세부 정보와 작업을 제공할 수 있습니다. 사용자가 관련 영역으로 이동하지 않도록 합니다. 예를 들어 사람들이 주식 기호 위젯을 클릭하거나 탭하면 주식 앱이 열리고 해당 기호에 대한 정보가 표시되는 페이지가 나타납니다. 마찬가지로, 사람들이 작은 주식 감시 목록 위젯을 클릭하거나 탭하면 앱이 열리고 전체 감시 목록이 표시됩니다. 더 큰 버전의 감시 목록 위젯에서 사용자가 하나의 기호를 누르거나 누르면 해당 기호를 표시하기 위해 재고가 열립니다.
>




![https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/widgets/images/multiple-tap-targets_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/widgets/images/multiple-tap-targets_2x.png)

**Avoid defining too many interaction targets.** A small widget supports a single target, but larger widgets can offer multiple targets. For example, the medium Notes widget can display several notes. When people click or tap one of them, the app opens to display that note. Although multiple interaction targets might make sense for your content, avoid offering so many that people have to spend time choosing the one they want.
> 너무 많은 상호 작용 대상을 정의하지 마십시오. 작은 위젯은 단일 대상을 지원하지만 큰 위젯은 여러 대상을 제공할 수 있습니다. 예를 들어, 중간 크기의 Notes 위젯은 여러 노트를 표시할 수 있습니다. 사람들이 그들 중 하나를 클릭하거나 탭하면, 그 노트를 표시하기 위해 앱이 열립니다. 여러 개의 상호작용 대상이 내용에 적합할 수 있지만, 너무 많이 제공하여 사람들이 원하는 대상을 선택하는 데 시간을 할애하지 않도록 하십시오.
>




**Let people know when authentication adds value.** If your widget provides additional functionality when someone is signed in to your app, make sure people know that. For example, an app that shows upcoming reservations might include a message like “Sign in to view reservations” when people are signed out.
> 인증이 가치를 추가할 때 사용자에게 알려줍니다. 다른 사용자가 앱에 로그인했을 때 위젯이 추가 기능을 제공하는 경우 사용자가 이를 알 수 있도록 합니다. 예를 들어, 예정된 예약을 보여주는 앱에는 사용자가 로그아웃할 때 "예약을 보려면 로그인"과 같은 메시지가 포함될 수 있습니다.
>




# **Interface design**

Widgets use vivid colors, rich images, and clear, crisp text that’s easy to read at a glance. A unique, beautiful widget not only provides useful information, it also can encourage people to feature it on their devices.
> 위젯은 선명한 색상, 풍부한 이미지, 한눈에 읽기 쉬운 선명하고 선명한 텍스트를 사용합니다. 독특하고 아름다운 위젯은 유용한 정보를 제공할 뿐만 아니라 사람들이 기기에 그것을 사용하도록 장려할 수 있다.
>




**Help people recognize your widget by including design elements linked to your brand’s identity.** Design elements like brand colors, typeface, and stylized glyphs can make a widget instantly recognizable. Take care to keep brand-related design elements from crowding out useful information or making your widget look out of place on the Home Screen.
> 브랜드의 아이덴티티에 연결된 디자인 요소를 포함하여 사람들이 위젯을 인식할 수 있도록 지원합니다. 브랜드 색상, 서체 및 양식화된 글리프와 같은 디자인 요소를 사용하면 위젯을 즉시 인식할 수 있습니다. 브랜드 관련 디자인 요소가 홈 스크린에서 유용한 정보를 대량으로 제공하거나 위젯이 어울리지 않게 보이지 않도록 주의하십시오.
>




**NOTE**When a widget appears in Notification Center in macOS or on the Home Screen in iOS, the system displays the app name below it. In Today View, the Lock Screen on iPhone, and the Home Screen in iPadOS, the app name doesn’t appear below a widget.
> 참고 위젯이 macOS의 Notification Center 또는 iOS의 홈 화면에 나타나면 시스템은 그 아래에 앱 이름을 표시합니다. Today View, iPhone의 잠금 화면 및 iPadOS의 홈 화면에서는 위젯 아래에 앱 이름이 표시되지 않습니다.
>




**Consider carefully before displaying a logo, wordmark, or app icon in your widget.** When you include brand-related design elements like colors and fonts, people seldom need your logo or app icon to help them recognize your widget. Also, the widget gallery displays your app name and icon when it lists the various types and sizes of widgets you offer. In some widgets — for example, those that display content from multiple sources — it may make sense to include a small logo in the top-right corner to subtly identify the app that provides the widget.
> 로고, 워드마크 또는 앱 아이콘을 위젯에 표시하기 전에 신중하게 고려하십시오. 색상 및 글꼴과 같은 브랜드 관련 디자인 요소를 포함할 때 위젯을 인식하는 데 도움이 되는 로고나 앱 아이콘이 필요한 경우는 거의 없습니다. 또한 위젯 갤러리는 사용자가 제공하는 다양한 위젯 유형 및 크기를 나열할 때 사용자의 앱 이름과 아이콘을 표시합니다. 일부 위젯(예: 여러 소스의 콘텐츠를 표시하는 위젯)에서는 오른쪽 상단 모서리에 작은 로고를 포함하여 위젯을 제공하는 앱을 미묘하게 식별할 수 있습니다.
>




**Aim for a comfortable density of information.** When content appears sparse, the widget can seem unnecessary; when content is too dense, the widget isn’t glanceable. If you have lots of information to include, avoid letting your widget become a collage of items that are difficult to parse. Seek ways to curate the content so that people can grasp the essential parts instantly and view relevant details at a longer look. You might also consider creating a larger widget and looking for places where you can replace text with graphics without losing clarity.
> 편안한 정보 밀도를 목표로 합니다. 콘텐츠가 희박하게 나타날 때 위젯이 불필요해 보일 수 있습니다. 콘텐츠가 너무 밀도가 높으면 위젯을 한눈에 볼 수 없습니다. 포함할 정보가 많은 경우 위젯이 구문 분석하기 어려운 항목의 콜라주가 되지 않도록 하십시오. 사람들이 중요한 부분을 즉시 파악하고 관련 세부 사항을 더 길게 볼 수 있도록 내용을 큐레이션하는 방법을 모색합니다. 더 큰 위젯을 만들고 명확성을 잃지 않고 텍스트를 그래픽으로 바꿀 수 있는 위치를 찾는 것도 고려할 수 있습니다.
>




**Use color judiciously.** Beautiful colors draw the eye, but they’re best when they don’t prevent people from absorbing a widget’s information at a glance. Use color to enhance a widget’s appearance without competing with its content. In your asset catalog, you can also specify the colors you want the system to use as it generates your widget’s editing-mode user interface.
> 색상을 신중하게 사용하십시오. 아름다운 색상은 눈길을 끌지만 위젯의 정보를 한 눈에 파악하는 데 방해가 되지 않을 때 가장 좋습니다. 색상을 사용하여 위젯의 내용과 경쟁하지 않고 위젯의 모양을 향상시킵니다. 자산 카탈로그에서 위젯의 편집 모드 사용자 인터페이스를 생성할 때 시스템에서 사용할 색상을 지정할 수도 있습니다.
>




