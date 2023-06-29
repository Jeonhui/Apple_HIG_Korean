# **[technologies] shareplay**

# SharePlay helps multiple people share activities — like viewing movies and listening to music — while they’re in a FaceTime call or Messages conversation.
> SharePlay를 사용하면 여러 사람이 FaceTime 통화 또는 메시지 대화 중에 영화 보기, 음악 듣기 등의 활동을 공유할 수 있습니다.
>




![https://developer.apple.com/design/human-interface-guidelines/images/intro/technologies/technology-Share-Play-intro_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/technologies/technology-Share-Play-intro_2x.png)

The system synchronizes app playback on all participating devices to enable seamless media sharing so everyone can enjoy the experience simultaneously.
> 이 시스템은 모든 참여 장치에서 앱 재생을 동기화하여 원활한 미디어 공유를 가능하게 하여 모든 사람이 동시에 경험을 즐길 수 있습니다.
>




**Let people know that you support SharePlay.** People often expect media playback experiences to be shareable, so indicate this capability in your UI. For example, you can use the `shareplay` SF Symbol to identify the content or experiences in your app that support SharePlay.
> 사용자가 SharePlay를 지원한다는 것을 알립니다. 미디어 재생 경험을 공유할 수 있을 것으로 기대하는 경우가 많으므로 UI에 이 기능을 표시합니다. 예를 들어 'Shareplay' SF 기호를 사용하여 SharePlay를 지원하는 앱의 콘텐츠 또는 경험을 식별할 수 있습니다.
>




Offer [Universal Purchase](https://developer.apple.com/support/universal-purchase/) to support SharePlay experiences among people running your app on different platforms. While sharing media during a FaceTime call, each participant views the content within your app running on their device. If a participant doesn’t have your app installed, SharePlay can help them download it from the App Store.
> 앱을 다른 플랫폼에서 실행하는 사람들 사이에서 SharePlay 경험을 지원하기 위해 범용 구매를 제안합니다. FaceTime 통화 중 미디어를 공유하는 동안 각 참가자는 자신의 장치에서 실행 중인 앱 내의 콘텐츠를 봅니다. 참가자가 앱을 설치하지 않은 경우 SharePlay를 통해 앱 스토어에서 다운로드할 수 있습니다.
>




# **Sharing activities**

An *activity* is an app-defined type of shareable experience. For example, an app that lets people view videos might define a separate activity for viewing each type of content — like movies, TV shows, and uploaded videos — and display a different description for each activity. You can define as many different activities as make sense in your app. For developer guidance, see [Inviting participants to share an activity](https://developer.apple.com/documentation/groupactivities/inviting-participants-to-share-an-activity).
> 활동은 공유 가능한 경험의 앱 정의 유형입니다. 예를 들어 동영상을 볼 수 있는 앱은 영화, TV 프로그램 및 업로드된 비디오와 같은 각 콘텐츠 유형을 보기 위한 별도의 활동을 정의하고 각 활동에 대한 다른 설명을 표시할 수 있습니다. 앱에서 타당한 만큼 다양한 활동을 정의할 수 있습니다. 개발자 지침은 활동 공유를 위해 참가자 초대를 참조하십시오.
>




**Briefly describe each activity.** When people receive an invitation to participate in an activity, your description helps them understand the experience they’re about to share. For example, a video-viewing app might associate its descriptive movie view with a movie-viewing activity. In this case, the descriptive view might display a movie’s title, a plot summary, and a poster image. Write a simple, meaningful description that’s short enough to avoid truncation.
> 각 활동에 대해 간략하게 설명하십시오. 사람들이 활동에 참여하라는 초대를 받을 때 사용자의 설명은 그들이 공유하려는 경험을 이해하는 데 도움이 됩니다. 예를 들어 비디오 보기 앱은 설명 동영상 보기를 동영상 보기 활동과 연결할 수 있습니다. 이 경우 설명 보기에는 영화 제목, 줄거리 요약 및 포스터 이미지가 표시될 수 있습니다. 잘라내기를 피할 수 있을 만큼 충분히 짧은 단순하고 의미 있는 설명을 작성하십시오.
>




**Make it easy to start sharing an activity.** If there’s no session available when people start a shareable activity, you can present UI that lets them start a group activity. In response, the system asks people if they want to share or continue the experience solo.
> 쉽게 활동 공유를 시작할 수 있습니다. 공유 가능한 활동을 시작할 때 세션을 사용할 수 없는 경우 그룹 활동을 시작할 수 있는 UI를 표시할 수 있습니다. 이에 대해, 이 시스템은 사람들에게 그들이 혼자서 경험을 공유하고 싶은지 아니면 계속하고 싶은지를 묻는다.
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/shareplay/images/shareplay_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/shareplay/images/shareplay_2x.png)

**Help people prepare to join a session before displaying the activity.** For example, if people must log in, download content, or make a payment before they can participate, display views that help them perform these tasks before showing the activity UI. Make these tasks as simple and effortless as possible so people can join the group activity quickly.
> 활동을 표시하기 전에 사용자가 세션에 참여할 준비를 하도록 도와줍니다. 예를 들어, 사용자가 참여하기 전에 로그인하거나 콘텐츠를 다운로드하거나 결제해야 하는 경우 활동 UI를 표시하기 전에 이러한 작업을 수행하는 데 도움이 되는 보기를 표시합니다. 사람들이 그룹 활동에 빠르게 참여할 수 있도록 이러한 작업을 가능한 한 간단하고 쉽게 만드십시오.
>




**If part of your app requires a subscription, consider ways to help nonsubscriber participants quickly join a group activity.** For example, you might offer temporary or provisional access to nonsubscribers or let an existing subscriber send a one-time pass to a friend. To make it easy for family members to share your content in a SharePlay experience, you can support [Family Sharing](https://developer.apple.com/design/human-interface-guidelines/technologies/in-app-purchase#enabling-family-sharing). If people can start a subscription during a SharePlay experience, present a streamlined version of your sign-up flow so they can join the activity without making others wait. For guidance, see [Auto-renewable subscriptions](https://developer.apple.com/design/human-interface-guidelines/technologies/in-app-purchase#auto-renewable-subscriptions).
> 앱의 일부에 가입이 필요한 경우 가입자가 아닌 참가자가 그룹 활동에 빠르게 참여할 수 있는 방법을 고려하십시오. 예를 들어, 가입자가 아닌 참가자에게 임시 또는 임시 액세스 권한을 제공하거나 기존 가입자가 친구에게 일회용 패스를 보낼 수 있도록 할 수 있습니다. 가족 구성원이 SharePlay 환경에서 사용자의 콘텐츠를 쉽게 공유할 수 있도록 가족 공유를 지원할 수 있습니다. SharePlay 경험 중에 구독을 시작할 수 있는 사용자는 다른 사용자를 기다리지 않고 활동에 참여할 수 있도록 간소화된 버전의 등록 흐름을 제시하십시오. 자세한 내용은 자동 갱신 구독을 참조하십시오.
>




**When possible, defer app tasks that might delay a shared activity.** For example, if your app needs to know a participant’s profile, consider asking for this information at a convenient time, like when playback pauses or finishes.
> 가능하면 공유 활동을 지연시킬 수 있는 앱 작업을 연기하십시오. 예를 들어, 앱이 참가자의 프로필을 알아야 하는 경우 재생이 일시 중지되거나 끝날 때와 같이 편리한 시간에 이 정보를 요청하는 것이 좋습니다.
>




**Use the term *SharePlay* correctly.** You can use *SharePlay* as a noun — as in "Join SharePlay" — and also as a verb when describing a direct action in your UI. For example, in a button or sheet that lets people share a movie-viewing activity, you can use a phrase like "SharePlay Movie." Avoid changing the term *SharePlay* in any way; for example, don’t use variations like *SharePlayed*, *SharePlays*, or *SharePlaying*.
> SharePlay라는 용어를 올바르게 사용하십시오. UI에서 직접 작업을 설명할 때 SharePlay를 명사로 사용할 수도 있고 동사로도 사용할 수 있습니다. 예를 들어 동영상 보기 활동을 공유할 수 있는 단추나 시트에서 "SharePlay Movie(동영상 공유)"와 같은 구문을 사용할 수 있습니다 SharePlay, SharePlays 또는 SharePlaying과 같은 변형을 사용하지 않도록 합니다.
>




**Support Picture in Picture (PiP) when possible.** On iPhone and iPad, people can open a shared video in a PiP window. On a Mac, a shared video opens in a background window that people can move into the foreground when they want to watch.
> 가능한 경우 PiP(Picture in Picture)를 지원합니다. 아이폰과 아이패드에서는 PiP 창에서 공유 비디오를 열 수 있습니다. Mac에서는 사람들이 보고 싶을 때 전경으로 이동할 수 있는 배경 창에 공유 비디오가 열립니다.
>



