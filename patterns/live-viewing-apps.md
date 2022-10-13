# **[patterns] live-viewing-apps**

# As you design a live-viewing app, focus on the content and creating fun, fluid interactions that encourage immersion in the live-viewing experience.
> 라이브 뷰잉 앱을 설계할 때 콘텐츠에 집중하고 라이브 뷰잉 경험에 몰입하도록 장려하는 재미있고 유동적인 상호 작용을 만드십시오.
>




![https://developer.apple.com/design/human-interface-guidelines/images/intro/patterns/pattern-live-viewing-intro-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/patterns/pattern-live-viewing-intro-dark_2x.png)

Live-viewing apps have some unique design challenges that set them apart from other tvOS apps. Above all, your app needs to elevate and prioritize live content. In every screen, draw people's attention to live content and make sure they can distinguish it from video-on-demand (VOD) content at a glance.
> 라이브뷰 앱은 다른 tvOS 앱과 차별화되는 몇 가지 독특한 디자인 과제를 안고 있다. 무엇보다도, 당신의 앱은 라이브 콘텐츠를 높이고 우선순위를 정해야 한다. 모든 화면에서 라이브 콘텐츠에 대한 사람들의 관심을 끌어 한 눈에 VOD(주문형 비디오) 콘텐츠와 구별할 수 있는지 확인합니다.
>




# **Best practices**

**Feature live content prominently and make it easy to access.** People come to your app to watch TV, so you want to minimize the interval between starting your app and playing content. When live content is in the first tab, people don't have to tap more than once to start viewing it.
> 라이브 콘텐츠를 눈에 띄게 제공하고 쉽게 액세스할 수 있습니다. 사람들은 TV를 보기 위해 당신의 앱에 오기 때문에, 당신은 당신의 앱을 시작하고 콘텐츠를 재생하는 간격을 최소화하기를 원한다. 라이브 콘텐츠가 첫 번째 탭에 있을 때, 사람들은 보기 시작하기 위해 두 번 이상 누를 필요가 없다.
>




**Let people tap once — or not at all — to start playback.** For example, you might display a focused Watch Now button on top of featured or recently viewed live content. When people tap this button, it immediately disappears and playback begins, replacing your app's UI with a full-screen, immersive viewing experience.
> 재생을 시작하려면 사용자가 한 번 누르거나 아예 누르지 않도록 합니다. 예를 들어, 기능 또는 최근에 본 라이브 콘텐츠 위에 지금 보기 단추가 포커스로 표시될 수 있습니다. 사람들이 이 버튼을 누르면, 그것은 즉시 사라지고 재생이 시작되며, 당신의 앱의 UI를 전체 화면, 몰입형 보기 환경으로 대체한다.
>




**Make sure live content looks live.** People need to be able to distinguish live content from VOD content. Although simply playing live content is the best way to make it feel live, you can also help people recognize live content by marking it in some way. For example, you might display other channels in a collection row titled "Live" and give each item a visual indicator — such as a badge, symbol, or sash — that identifies it as live.
> 라이브 콘텐츠가 라이브로 표시되는지 확인합니다. 사람들은 라이브 콘텐츠를 VOD 콘텐츠와 구별할 수 있어야 한다. 라이브 콘텐츠를 단순히 재생하는 것이 라이브로 느껴지도록 하는 가장 좋은 방법이지만, 어떤 방식으로든 표시하여 라이브 콘텐츠를 인식하도록 도울 수도 있습니다. 예를 들어 "라이브"라는 제목의 컬렉션 행에 다른 채널을 표시하고 각 항목에 라이브로 식별할 수 있는 시각적 표시기(예: 배지, 기호 또는 새시)를 제공할 수 있습니다.
>




**Consider indicating the progress of currently playing live content.** People appreciate knowing where they'll land when they jump into in-progress live content. You can use a progress bar or other indicator to show people how much content remains.
> 현재 라이브 콘텐츠를 재생하는 진행 상황을 표시하는 것을 고려해 보십시오. 사람들은 진행 중인 라이브 콘텐츠에 뛰어들 때 어디에 착륙할지 아는 것에 감사한다. 진행률 표시줄 또는 기타 표시기를 사용하여 사용자에게 남은 콘텐츠 양을 표시할 수 있습니다.
>




**Give people additional actions and viewing alternatives.** In addition to playback, which always needs to be the primary action, make it easy for people to record, restart, download, and perform other actions that you support. Display these actions in the same order throughout your app — for example, Watch, Start Over, Record, and Favorite. Also, if the currently playing content is playing again at other times, show this information so that people can schedule their viewing.
> 사용자에게 추가 작업 및 보기 대안을 제공합니다. 항상 기본 작업이어야 하는 재생 외에도 사용자가 지원하는 작업을 쉽게 기록, 다시 시작, 다운로드 및 수행할 수 있습니다. 이러한 작업을 시청, 다시 시작, 녹화 및 즐겨찾기와 같은 순서로 앱 전체에 표시합니다. 또한 현재 재생 중인 콘텐츠가 다른 시간에 다시 재생되는 경우 이 정보를 표시하여 사용자가 보기를 예약할 수 있도록 합니다.
>




**Consider using a content footer for browsing channels during playback.** A content footer lets people browse without taking them out of the live playback experience. If you decide to use a content footer, be sure to:
> 재생 중에 채널 검색에 콘텐츠 바닥글을 사용하는 것이 좋습니다. 콘텐츠 바닥글을 사용하면 실시간 재생 경험에서 사용자를 꺼내지 않고 찾아볼 수 있습니다. 내용 바닥글을 사용하려면 다음을 수행하십시오.
>




- Give it a subtle treatment, such as a darkening, to keep text legible and help all items remain visually distinct from the content playing behind it.
- >  텍스트를 읽기 쉽게 하고 모든 항목이 텍스트 뒤에서 재생되는 내용과 시각적으로 구별되도록 어두운 색상과 같은 미묘한 처리를 합니다.

- Make it easy for people to identify the thumbnail that represents the currently playing content by, for example, badging the thumbnail or tinting its progress bar.
- >  예를 들어, 미리 보기를 배지하거나 진행률 표시줄을 색칠하여 현재 재생 중인 내용을 나타내는 미리 보기를 쉽게 식별할 수 있습니다.

- Match the categories in the content footer to those in your electronic program guide (for related guidance, see [EPG experience](https://developer.apple.com/design/human-interface-guidelines/patterns/live-viewing-apps#epg-experience).
- >  내용 바닥글의 범주를 전자 프로그램 안내서의 범주와 일치시킵니다(관련 지침은 EPG 경험 참조).

- Design a simple, predictable way for people to invoke and dismiss the content footer — for example, if swiping up invokes the footer, people would expect swiping down to dismiss it.
- >  사용자가 내용 바닥글을 호출하고 해제할 수 있는 간단하고 예측 가능한 방법을 설계하십시오. 예를 들어, 바닥글을 스와이프하면 사용자가 해당 바닥글을 스와이프하여 삭제할 것으로 예상할 수 있습니다.


**Provide instant visual feedback when people change channels.** Immediately providing feedback after a channel change is essential for two reasons. First, people need confirmation that they've arrived at the channel they want. Second, providing feedback can give the streaming content some time to load.
> 사람들이 채널을 변경할 때 즉각적인 시각적 피드백을 제공합니다. 채널 변경 후 즉시 피드백을 제공하는 것은 두 가지 이유로 필수적입니다. 먼저, 사람들은 그들이 원하는 채널에 도착했다는 확인이 필요하다. 둘째, 피드백을 제공하면 스트리밍 콘텐츠를 로딩하는 데 약간의 시간을 할애할 수 있습니다.
>




**Match audio to the current context.** When people start playing live content, they expect the audio to match even if they switch to browsing while the content plays in the background. However, when people navigate away from the live tab in your app, they leave the live-viewing context, so audio should stop.
> 오디오를 현재 컨텍스트와 일치시킵니다. 사람들이 라이브 콘텐츠를 재생하기 시작하면 콘텐츠가 백그라운드에서 재생되는 동안 브라우징으로 전환하더라도 오디오가 일치할 것으로 기대합니다. 그러나 앱의 라이브 탭에서 벗어나면 라이브 보기 컨텍스트에서 벗어나므로 오디오가 중단되어야 합니다.
>




# **EPG experience**

Live-viewing apps typically provide an electronic program guide (EPG) that contains information about scheduled programming. Follow these guidelines to give people a streamlined EPG experience that feels designed specifically for your live-viewing app.
> 라이브 뷰잉 앱은 일반적으로 예약된 프로그래밍에 대한 정보를 포함하는 전자 프로그램 가이드(EPG)를 제공합니다. 라이브 뷰잉 앱을 위해 특별히 설계된 것처럼 느껴지는 능률적인 EPG 경험을 사람들에게 제공하려면 다음 지침을 따르십시오.
>




**Prominently display current information and make it easy to return to playback.** When people first open the EPG, the current program, channel, and time needs to be easy to spot so they can instantly return to the current channel.
> 현재 정보를 눈에 띄게 표시하고 재생으로 쉽게 돌아갈 수 있습니다. 사람들이 EPG를 처음 열 때, 현재 프로그램, 채널, 시간을 쉽게 발견할 수 있어야 그들이 즉시 현재 채널로 돌아갈 수 있다.
>




**Make browsing the EPG effortless.** A typical EPG contains a lot of information, so it's important to help people page, scroll, or jump through it easily. Also consider providing a My Channels group or a Favorites group that gives people quick access to the content they view most often.
> EPG를 쉽게 탐색할 수 있습니다. 일반적인 EPG에는 많은 정보가 포함되어 있으므로 사람들이 쉽게 페이지를 보거나 스크롤하거나 탐색할 수 있도록 돕는 것이 중요합니다. 또한 가장 자주 보는 콘텐츠에 빠르게 액세스할 수 있는 내 채널 그룹 또는 즐겨찾기 그룹을 제공하는 것도 고려해 보십시오.
>




**Group content into familiar categories to help people find it more easily.** For example, you might use categories like Movies, TV Shows, Kids, Sports, and Popular. If your app includes a content footer, organize content thumbnails using the same categories as in the EPG.
> 콘텐츠를 익숙한 범주로 그룹화하여 사람들이 보다 쉽게 찾을 수 있도록 합니다. 예를 들어 영화, TV 프로그램, 어린이, 스포츠 및 인기 있는 범주를 사용할 수 있습니다. 앱에 콘텐츠 바닥글이 포함된 경우 EPG와 동일한 범주를 사용하여 콘텐츠 미리 보기를 구성합니다.
>




**Let people browse the EPG without leaving their current content.** For example, you can continue playing content in a picture-in-picture (PiP) mode or in the background while people browse the EPG.
> 사람들이 현재 콘텐츠를 남기지 않고 EPG를 탐색할 수 있도록 합니다. 예를 들어 사용자가 EPG를 검색하는 동안 PiP(Picture-in-Picture) 모드 또는 백그라운드에서 콘텐츠를 계속 재생할 수 있습니다.
>




# **Cloud DVR**

If you support digital video recording (DVR) in the cloud, follow these guidelines to provide a great recording experience in your live-viewing app.
> 클라우드에서 디지털 비디오 녹화(DVR)를 지원하는 경우 다음 지침을 따라 라이브 뷰잉 앱에서 훌륭한 녹화 환경을 제공하십시오.
>




**Let people start and stop recording from the info panel.** While live-streaming, people want to reveal the info panel to start recording immediately.
> 사람들이 정보 패널에서 녹화를 시작하거나 중지할 수 있습니다. 라이브 스트리밍을 하는 동안, 사람들은 즉시 녹화를 시작하기 위해 정보 패널을 공개하기를 원한다.
>




**Let people record a future program in a view that provides details about the content.** Also, give people the option to record only that program or all future episodes.
> 사용자가 내용에 대한 세부 정보를 제공하는 보기에 향후 프로그램을 녹화하도록 합니다. 또한, 사람들에게 그 프로그램만 녹화하거나 미래의 모든 에피소드를 녹화할 수 있는 옵션을 제공합니다.
>




**Help people adapt the recording experience to their needs.** Let people specify precisely what they want to record, such as only the current episode, only new episodes, or only games that involve specific teams.
> 녹음 경험을 필요에 맞게 조정할 수 있도록 지원합니다. 사람들이 현재 에피소드만, 새로운 에피소드만, 특정 팀이 참여하는 게임만과 같이 녹음할 내용을 정확하게 지정하도록 합니다.
>




**Allow playback and other content-specific actions within your cloud DVR area.** When people open a view that displays content details in your cloud DVR section, let them play or delete content and, if applicable, adjust recording settings.
> 클라우드 DVR 영역 내에서 재생 및 기타 콘텐츠 관련 작업을 허용합니다. 클라우드 DVR 섹션에서 콘텐츠 세부 정보를 표시하는 보기를 열면 해당 사용자가 콘텐츠를 재생하거나 삭제하도록 하고, 해당되는 경우 녹화 설정을 조정합니다.
>




**Consider offering a control that lets people manage cloud DVR settings.** For example, you might let people delete recordings they've already watched or content that's older than a certain number of days. Ideally, help people avoid running out of space by letting them set up automatic storage management, which overwrites the oldest or already viewed content.
> 사람들이 클라우드 DVR 설정을 관리할 수 있는 컨트롤을 제공하는 것을 고려해 보십시오. 예를 들어, 사용자가 이미 시청한 녹화나 특정 일보다 오래된 콘텐츠를 삭제하도록 허용할 수 있습니다. 자동 스토리지 관리를 설정하여 가장 오래되었거나 이미 본 콘텐츠를 덮어쓰도록 하여 공간 부족을 방지하는 것이 이상적입니다.
>




# **Platform considerations**

*Not supported in iOS, iPadOS, macOS, or watchOS.*
> iOS, iPadOS, macOS 또는 watch에서 지원되지 않음OS.
>



