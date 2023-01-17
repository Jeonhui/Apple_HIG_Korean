# **[technologies-carplay] introduction**

# iPhone apps that appear on the car’s built-in display are optimized for the driving environment and meet the unique demands of the car.
> 자동차 내장 디스플레이에 등장하는 아이폰 앱은 주행 환경에 최적화돼 자동차 특유의 수요를 충족시킨다.
>




![https://developer.apple.com/design/human-interface-guidelines/images/intro/technologies/technology-CarPlay-intro_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/technologies/technology-CarPlay-intro_2x.png)

The best apps support brief interactions and never command the driver’s attention. On-screen information is minimal, relevant, and requires little decision making. Voice interaction using Siri enables drivers to control many apps without taking their hands off the steering wheel or eyes off the road. Well-known iOS paradigms, including interface elements, icons, text appearance, and terminology provide a familiar, intuitive experience.
> 최고의 앱은 짧은 상호 작용을 지원하고 운전자의 주의를 끌지 못한다. 화면상의 정보는 최소한이며 관련성이 있으며 의사결정이 거의 필요하지 않다. 시리를 이용한 음성 상호작용은 운전자가 운전대에서 손을 떼거나 도로에서 눈을 떼지 않고도 많은 앱을 제어할 수 있게 해준다. 인터페이스 요소, 아이콘, 텍스트 모양 및 용어를 포함한 잘 알려진 iOS 패러다임은 친숙하고 직관적인 경험을 제공합니다.
>




iPhone apps like Maps, Messages, Music, and Phone display car-appropriate interfaces that look great in CarPlay and are easy to operate while driving. The audio app, automaker app, messaging app, or Voice over Internet Protocol (VoIP) app you design should be just as simple and easy to operate.
> 지도, 메시지, 음악, 전화와 같은 아이폰 앱은 자동차에 적합한 인터페이스를 보여주는데, 이 인터페이스는 자동차 플레이에 잘 어울리며 운전 중에도 조작하기 쉽다. 당신이 디자인하는 오디오 앱, 자동차 회사 앱, 메시징 앱 또는 VoIP(Voice over Internet Protocol) 앱은 단순하고 조작하기 쉬워야 한다.
>




# **Audio apps**

Apps that serve audio content (audiobooks, Internet radio, news, podcasts, and sports, for example) can expose that content through the car’s built-in display. These apps supply an app icon for the CarPlay Home screen (in addition to a corresponding app icon on the iPhone Home screen); a hierarchical list of content to display in a tabbed browser; and information for a Now Playing screen. The system presents this information in an interface optimized for CarPlay, using a template that resembles the Music app. Although your app's basic appearance is handled by the system, there are still many design considerations for ensuring a great user experience.
> 오디오 콘텐츠를 제공하는 앱(예: 오디오북, 인터넷 라디오, 뉴스, 팟캐스트 및 스포츠)은 자동차의 내장 디스플레이를 통해 해당 콘텐츠를 노출할 수 있다. 이러한 앱은 자동차 재생 홈 화면에 대한 앱 아이콘(iPhone 홈 화면에 해당하는 앱 아이콘 외), 탭으로 표시할 콘텐츠의 계층 목록, 지금 재생 화면에 대한 정보를 제공합니다. 시스템은 음악 앱과 유사한 템플릿을 사용하여 CarPlay에 최적화된 인터페이스로 이 정보를 제공합니다. 비록 당신의 앱의 기본 모양은 시스템에 의해 처리되지만, 훌륭한 사용자 경험을 보장하기 위한 많은 설계 고려사항들이 여전히 있다.
>




For developer guidance, see [CarPlay](http://developer.apple.com/carplay/) and [MediaPlayer](https://developer.apple.com/documentation/mediaplayer).

# **Structuring and providing data**

Audio apps must provide a complete navigable hierarchy of audio information—radio stations, albums, artists, titles, and so forth. The system uses this information to populate tabs and tables in the CarPlay interface, and to respond to user actions like track selection and media playback.
> 오디오 앱은 라디오 방송국, 앨범, 아티스트, 제목 등과 같은 완전한 탐색 가능한 오디오 정보 계층을 제공해야 합니다. 시스템은 이 정보를 사용하여 CarPlay 인터페이스의 탭과 테이블을 채우고 트랙 선택 및 미디어 재생과 같은 사용자 작업에 응답합니다.
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/carplay/images/AudioApp_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/carplay/images/AudioApp_2x.png)

**Always provide content, even when data is unavailable.** Drivers occasionally encounter poor network reception. If data is unavailable, provide placeholder or cached content so the system can still generate the interface for your app. Supply updated content once it becomes available.
> 데이터를 사용할 수 없는 경우에도 항상 컨텐츠를 제공하십시오. 드라이버는 때때로 네트워크 수신 상태가 좋지 않습니다. 데이터를 사용할 수 없는 경우 시스템이 앱의 인터페이스를 계속 생성할 수 있도록 자리 표시자 또는 캐시된 콘텐츠를 제공합니다. 업데이트된 콘텐츠를 사용할 수 있게 되면 제공합니다.
>




**Limit your content hierarchy to three levels or fewer.** The less navigation required to reach content, the better. Although the system permits a maximum depth of five levels, three levels or fewer is recommended. For example, Artists > Albums > Songs, or Playlists > Songs.
> 콘텐츠 계층을 3단계 이하로 제한합니다. 콘텐츠에 도달하는 데 필요한 탐색이 적을수록 좋습니다. 시스템은 최대 5단계 깊이를 허용하지만 3단계 이하의 깊이가 권장됩니다. 예를 들어 아티스트 > 앨범 > 노래 또는 재생 목록 > 노래입니다.
>




**Use multiple tabs to organize content and ease navigation.** The tab bar at the top of the screen flattens your app’s hierarchy and lets the user quickly switch between different categories of content.
> 여러 탭을 사용하여 콘텐츠를 구성하고 쉽게 탐색할 수 있습니다. 화면 상단의 탭 표시줄은 앱의 계층을 평평하게 만들고 사용자가 다른 범주의 콘텐츠를 빠르게 전환할 수 있도록 합니다.
>




**Show the most relevant content first.** Anticipate information and actions most important to the driver, and present it first to reduce scrolling and navigation. Music, for example, prioritizes recently added music and playlists, and presents them at the top of the first tab. In Podcasts, the top of the first tab lets you instantly pause or resume the active episode.
> 가장 관련성이 높은 콘텐츠를 먼저 보여준다. 운전자에게 가장 중요한 정보와 행동을 예상하고, 스크롤과 내비게이션을 줄이기 위해 먼저 제시한다. 예를 들어, 음악은 최근에 추가된 음악과 재생 목록의 우선 순위를 지정하고 첫 번째 탭의 맨 위에 표시합니다. 팟캐스트에서 첫 번째 탭의 맨 위에서 활성 에피소드를 즉시 일시 중지하거나 다시 시작할 수 있습니다.
>




**Include single-touch playback actions at the top level of your hierarchy.** Easy one-touch playback options such as Shuffle and Resume add value and convenience to your app.
> 단일 터치 재생 작업을 계층의 최상위 수준에 포함합니다. 셔플 및 재개와 같은 쉬운 원터치 재생 옵션은 앱에 가치와 편의성을 더해줍니다.
>




**Intelligently filter content when the vehicle is moving.** Certain cars may cause CarPlay to truncate lists of content when the vehicle is in motion or has exceeded a certain speed. Consider displaying a curated set of essential information and options when this mode becomes active.
> 차량이 이동 중일 때 콘텐츠를 지능적으로 필터링합니다. 특정 차량은 차량이 이동 중이거나 특정 속도를 초과할 때 CarPlay가 콘텐츠 목록을 잘라낼 수 있습니다. 이 모드가 활성화되면 필수 정보 및 옵션의 큐레이션된 집합을 표시하는 것이 좋습니다.
>




**Supply succinct titles and descriptions.** Always include a title, like an album name or track name. If it makes sense, provide a subtitle with additional information, such as the artist or composer name. Keep titles and subtitles short so they can be scanned quickly and peripherally.
> 간결한 제목과 설명을 입력하십시오. 항상 앨범 이름이나 트랙 이름과 같은 제목을 포함하십시오. 이해가 되는 경우 아티스트 또는 작곡가 이름과 같은 추가 정보가 포함된 부제를 제공합니다. 제목과 자막을 짧게 유지하여 신속하고 주변적으로 스캔할 수 있습니다.
>




**Provide supplementary artwork.** Imagery appearing in the navigation hierarchy, such as album art, improves the appearance of your app and makes content easier to locate at a glance.
> 보조 아트워크를 제공합니다. 앨범 아트와 같은 탐색 계층에 나타나는 이미지는 앱의 모양을 개선하고 콘텐츠를 한 눈에 쉽게 찾을 수 있도록 합니다.
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/carplay/images/icon_explicit_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/carplay/images/icon_explicit_2x.png)

**Denote explicit content.** CarPlay displays an indicator when content is marked as explicit, making it easy for people to detect and skip.
> 명시적인 내용을 나타냅니다. CarPlay는 내용이 명시적으로 표시될 때 표시기를 표시하여 사람들이 쉽게 검색하고 건너뛸 수 있도록 합니다.
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/carplay/images/icon_iCloud_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/carplay/images/icon_iCloud_2x.png)

**Denote streaming content.** CarPlay displays an indicator when content is marked as streaming. Some users have cellular data usage limits, so be mindful when streaming content over the cellular network.
> 스트리밍 콘텐츠를 나타냅니다. 카플레이는 콘텐츠가 스트리밍으로 표시될 때 표시기를 표시합니다. 일부 사용자는 셀룰러 데이터 사용 제한이 있으므로 셀룰러 네트워크를 통해 콘텐츠를 스트리밍할 때 주의해야 합니다.
>




**Don't require sign in or configuration steps in CarPlay.** Audio apps in CarPlay are about consumption. Don't ask the user to perform setup steps on the car's display. It's highly probable your app will be launched on iPhone before it's used in CarPlay, so your iPhone experience should ensure setup is complete. If a setup step does become necessary in CarPlay, gracefully handle the situation without encouraging the user to pick up their phone. For example, consider offering cached audio the user can play without signing in.
> CarPlay에서 로그인 또는 구성 단계가 필요하지 않습니다. CarPlay의 오디오 앱은 소비에 관한 것입니다. 사용자에게 차량 디스플레이에 대한 설정 단계를 수행하도록 요청하지 마십시오. 당신의 앱은 CarPlay에서 사용되기 전에 iPhone에서 실행될 가능성이 높기 때문에, 당신의 iPhone 경험은 설정이 완료되었음을 보장해야 한다. CarPlay에서 설정 단계가 필요한 경우 사용자가 전화를 받도록 권장하지 않고 상황을 우아하게 처리하십시오. 예를 들어, 사용자가 로그인하지 않고 재생할 수 있는 캐시된 오디오를 제공하는 것을 고려해 보십시오.
>




For developer guidance, see [MPPlayableContentDataSource](https://developer.apple.com/documentation/mediaplayer/mpplayablecontentdatasource).

# **Playing media**

The system automatically shows a Now Playing screen when playing audio content, and populates it with the data your app provides.
> 시스템은 오디오 콘텐츠를 재생할 때 자동으로 지금 재생 화면을 표시하고 앱이 제공하는 데이터로 채웁니다.
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/carplay/images/NowPlaying_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/carplay/images/NowPlaying_2x.png)

**Provide useful, accurate information and controls when playing audio.** The Now Playing screen can show a title, artist, album art, rating, and playback progress. It can also include controls for liking, disliking, and bookmarking the playing audio. Information should be updated whenever playback begins and ends.
> 오디오를 재생할 때 유용하고 정확한 정보와 컨트롤을 제공합니다. 지금 재생 화면에는 제목, 음악가, 앨범 아트, 등급 및 재생 진행률이 표시될 수 있습니다. 또한 재생 중인 오디오를 좋아하거나 싫어하거나 북마크하는 컨트롤을 포함할 수 있습니다. 재생이 시작되고 끝날 때마다 정보를 업데이트해야 합니다.
>




**Don’t redefine the meaning of playback controls.** A physical Play button in the car, for example, should begin playing audio, not skip to the next track.
> 재생 컨트롤의 의미를 재정의하지 마십시오. 예를 들어, 자동차의 물리적 재생 버튼은 다음 트랙으로 건너뛰지 말고 오디오를 재생하기 시작해야 합니다.
>




**Resume audio playback when appropriate after an interruption.** Temporary interruptions like incoming phone calls are resumable. Permanent interruptions, like a music playlist initiated by Siri, are nonresumable. When a resumable interruption occurs, your app should resume playback when the interruption ends if audio was actively playing when the interruption started. An app that is not playing audio when an interruption occurs has nothing to resume.
> 중단 후 적절한 경우 오디오 재생을 다시 시작합니다. 걸려오는 전화와 같은 일시적인 중단은 다시 시작할 수 있습니다. 시리가 시작한 음악 재생 목록과 같은 영구적인 중단은 재개할 수 없다. 재개 가능한 중단이 발생하면 중단이 시작되었을 때 오디오가 재생 중이었다면 중단이 종료될 때 앱이 재생을 재개해야 합니다. 중단이 발생할 때 오디오가 재생되지 않는 앱은 다시 시작할 수 없습니다.
>




For developer guidance, see [MPPlayableContentDelegate](https://developer.apple.com/documentation/mediaplayer/mpplayablecontentdelegate) and [MPNowPlayingInfoCenter](https://developer.apple.com/documentation/mediaplayer/mpnowplayinginfocenter).

# **Automaker apps**

Automakers can design custom apps that provide information, expose useful functionality, and control built-in vehicle features—like climate controls, GPS, and the radio—without leaving the CarPlay experience.
> 자동차 제조업체는 CarPlay 경험을 그대로 유지하면서 정보를 제공하고 유용한 기능을 노출하며 실내 온도 조절 장치, GPS 및 라디오와 같은 내장된 차량 기능을 제어하는 사용자 지정 앱을 설계할 수 있습니다.
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/carplay/images/AutomakerApp_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/carplay/images/AutomakerApp_2x.png)

**Limit controls and content to what's relevant in the car.** Exposing every feature of your iPhone app through CarPlay can make your app more complex and less safe to use while driving. Don’t offer features that aren’t useful to drivers.
> 제어 기능과 콘텐츠를 자동차와 관련된 것으로 제한합니다. CarPlay를 통해 iPhone 앱의 모든 기능을 노출하면 앱이 더 복잡해지고 운전 중 안전하지 않게 될 수 있습니다. 운전자에게 유용하지 않은 기능을 제공하지 마십시오.
>




**Prefer standard controls.** A subset of system-provided user interface controls are optimized for CarPlay, including buttons, labels, navigation bars, tab bars, and tables. See [System elements](../technologies/carplay/system-elements). Displaying interface controls that don't match the visual style of other CarPlay apps can result in a fragmented and confusing user experience.
> 표준 컨트롤을 선호합니다. 버튼, 레이블, 탐색 모음, 탭 모음 및 테이블을 포함하여 시스템에서 제공하는 사용자 인터페이스 컨트롤의 하위 집합이 CarPlay에 최적화되어 있습니다. 시스템 요소를 참조하십시오. 다른 CarPlay 앱의 시각적 스타일과 일치하지 않는 인터페이스 컨트롤을 표시하면 파편화되고 혼란스러운 사용자 경험을 초래할 수 있습니다.
>




**Avoid redesigning standard controls.** The system-provided controls offer consistency and are optimized for legibility and interactivity in the car. If you must design custom versions of standard controls, make sure they’re similar in appearance to standard CarPlay controls, and large enough to see and interact with while driving.
> 표준 컨트롤을 재설계하지 마십시오. 시스템에서 제공하는 컨트롤은 일관성을 제공하며 차량 내 가독성과 상호 작용성에 최적화되어 있습니다. 표준 컨트롤의 사용자 지정 버전을 설계해야 하는 경우 표준 CarPlay 컨트롤과 모양이 비슷하고 운전 중에 보고 상호 작용할 수 있을 만큼 충분히 큰지 확인하십시오.
>




**Never mimic the design of the car's native interface.** Your app should have the familiar look and feel of other CarPlay apps.
> 절대로 자동차의 네이티브 인터페이스의 디자인을 모방하지 마십시오. 당신의 앱은 다른 카플레이 앱과 친숙한 모양과 느낌을 가져야 합니다.
>




For related guidance, see [Visual design](../technologies/carplay/visual-design).

# **Messaging and VoIP apps**

Messaging and VoIP apps use Siri and are exclusively voice-driven. They don’t present interfaces to the user, so no interface design is necessary that’s specific to CarPlay.
> 메시징 및 VoIP 앱은 시리를 사용하며 음성으로만 구동됩니다. 그들은 사용자에게 인터페이스를 제공하지 않기 때문에 CarPlay에 특화된 인터페이스 설계가 필요하지 않습니다.
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/carplay/images/Message_siri_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/carplay/images/Message_siri_2x.png)

**Support both reading and composing messages.** A messaging app optimized for CarPlay must allow the user to read and compose messages using only their voice.
> 메시지 읽기와 작성을 모두 지원합니다. CarPlay에 최적화된 메시징 앱은 사용자가 음성만으로 메시지를 읽고 작성할 수 있도록 해야 합니다.
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/carplay/images/MessageApp_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/carplay/images/MessageApp_2x.png)

**Enable CarPlay notifications.** A messaging app must explicitly opt in for its notifications to appear in CarPlay. For developer guidance, see [UNNotificationCategoryOptionAllowInCarPlay](https://developer.apple.com/documentation/usernotifications/unnotificationcategoryoptions/unnotificationcategoryoptionallowincarplay).
> CarPlay 알림을 활성화합니다. 메시지 앱은 알림이 CarPlay에 나타나도록 명시적으로 선택해야 합니다. 개발자 지침은 UNNotification Category 옵션 AllowInCarPlay를 참조하십시오.
>




**Display only message notifications.** Categorize your messaging notifications in a way that segregates them from other types of notifications.
> 메시지 통지만 표시합니다. 메시지 통지를 다른 유형의 통지와 구분하는 방식으로 분류합니다.
>




**Enable the appropriate Siri functions if your app supports VoIP.** To work with CarPlay, a VoIP app must allow the user to search the call history and start audio calls using Siri. For developer guidance, see [INSearchCallHistoryIntentIdentifier](https://developer.apple.com/documentation/sirikit/insearchcallhistoryintentidentifier), and [INStartAudioCallIntentIdentifier](https://developer.apple.com/documentation/sirikit/instartaudiocallintentidentifier).
> 당신의 앱이 VoIP를 지원한다면 적절한 Siri 기능을 활성화하세요. CarPlay를 사용하려면, VoIP 앱은 사용자가 Siri를 사용하여 통화 내역을 검색하고 오디오 통화를 시작할 수 있도록 해야 합니다. 개발자 지침은 INSearch 통화 기록을 참조하십시오IntentIdentifier 및 INTestart오디오 호출 의도 식별자입니다.
>



