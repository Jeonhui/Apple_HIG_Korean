# **[components-status] progress-indicators**

## Progress indicators let people know that your app isn’t stalled while it loads content or performs lengthy operations.
> 진행률 표시기는 앱이 콘텐츠를 로드하거나 긴 작업을 수행하는 동안 사용자의 앱이 정지되지 않았음을 알려줍니다.
>




![https://developer.apple.com/design/human-interface-guidelines/images/intro/components/progress-indicators-intro-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/components/progress-indicators-intro-dark_2x.png)

Some progress indicators also give people a way to estimate how long they have to wait for something to complete. All progress indicators are transient, appearing only while an operation is ongoing and disappearing after it completes.
> 일부 진행률 지표는 또한 사람들에게 어떤 것이 완료될 때까지 얼마나 기다려야 하는지 추정할 수 있는 방법을 제공한다. 모든 진행률 표시기는 일시적이며, 작업이 진행 중일 때만 나타나고 완료된 후에는 사라집니다.
>




Because the duration of an operation is either known or unknown, there are two types of progress indicators:
> 작업 기간을 알 수 없거나 알 수 없기 때문에 진행률 표시기에는 두 가지 유형이 있습니다.
>




- *Determinate*, for a task with a well-defined duration, such as a file conversion.
- >  파일 변환과 같이 기간이 잘 정의된 태스크에 대해 결정합니다.

- *Indeterminate*, for unquantifiable tasks, such as loading or synchronizing complex data.
- >  복잡한 데이터 로드 또는 동기화와 같은 정량화할 수 없는 작업에 대해 결정하지 않습니다.


# **Best practices**

**When possible, use a determinate progress indicator.** An indeterminate progress indicator shows that a process is occurring, but it doesn’t help people estimate how long a task will take. A determinate progress indicator can help people decide whether to do something else while waiting for the task to complete, restart the task at a different time, or abandon the task.
> 가능하면 확정된 진행률 표시기를 사용하십시오. 불확실한 진행률 표시기는 프로세스가 발생하고 있음을 보여주지만 작업에 소요되는 시간을 예측하는 데는 도움이 되지 않습니다. 결정된 진행률 표시기는 작업이 완료될 때까지 기다리면서 다른 작업을 수행할지, 다른 시간에 작업을 다시 시작할지 또는 작업을 포기할지 결정하는 데 도움이 됩니다.
>




**Be as accurate as possible when reporting advancement in a determinate progress indicator.** Consider evening out the pace of advancement to help people feel confident about the time needed for the task to complete. Showing 90 percent completion in five seconds and the last 10 percent in 5 minutes can make people wonder if your app is still working and can even feel deceptive.
> 결정적인 진행률 지표로 진행 상황을 보고할 때는 가능한 한 정확해야 한다. 사람들이 작업을 완료하는 데 필요한 시간에 대해 확신을 가질 수 있도록 진행 속도를 저녁에 고려해야 한다. 5초 안에 90%가 완료되고 마지막 10%가 5분 안에 완료되는 것을 보여주는 것은 사람들로 하여금 당신의 앱이 여전히 작동하고 있는지 궁금하게 만들 수 있고 심지어 기만적이라고 느낄 수도 있다.
>




**Keep progress indicators moving so people know something is continuing to happen.** People tend to associate a stationary indicator with a stalled process or a frozen app. If a process stalls for some reason, provide feedback that helps people understand the problem and what they can do about it.
> 사람들이 무언가가 계속해서 일어나고 있다는 것을 알 수 있도록 진행률 표시기를 계속 움직여라. 사람들은 정지 상태의 표시기를 프로세스나 정지된 앱과 연관시키는 경향이 있다. 어떤 이유로 인해 프로세스가 중단되는 경우 사용자가 문제를 이해하고 문제에 대해 수행할 수 있는 작업을 지원하는 피드백을 제공합니다.
>




**When possible, switch a progress bar from indeterminate to determinate.** If an indeterminate process reaches a point where you can determine its duration, switch to a determinate progress bar. People generally prefer a determinate progress indicator, because it helps them gauge what’s happening and how long it will take.
> 가능한 경우 진행 표시줄을 incertificate에서 determinate로 전환하고, incertificate 프로세스가 지속 시간을 결정할 수 있는 지점에 도달하면 determinated progress bar로 전환합니다. 사람들은 일반적으로 결정적인 진전 지표를 선호하는데, 이는 그들이 무슨 일이 일어나고 얼마나 오래 걸릴지 가늠하는 데 도움이 되기 때문이다.
>




**Don’t switch from the circular style to the bar style.** Spinners and progress bars are different shapes and sizes, so transitioning between them can disrupt your interface and confuse people.
> 원형 스타일에서 막대 스타일로 전환하지 마십시오. 스피너와 프로그레스 막대는 모양과 크기가 다르기 때문에 이들 사이를 전환하면 인터페이스가 중단되고 사람들을 혼란스럽게 할 수 있습니다.
>




**If it’s helpful, display a description that provides additional context for the task.** Be accurate and succinct. Avoid vague terms like *loading* or *authenticating* because they seldom add value.
> 도움이 될 경우 작업에 대한 추가 컨텍스트를 제공하는 설명을 표시합니다. 정확하고 간결해야 합니다. 로드 또는 인증과 같은 모호한 용어는 거의 추가되지 않으므로 사용하지 마십시오.
>




**Display a progress indicator in a consistent location.** Choosing a consistent location for a progress indicator helps people reliably find the status of an operation across platforms or within or between apps.
> 일정한 위치에 진행률 표시기를 표시합니다. 진행률 표시기의 일관된 위치를 선택하면 플랫폼 간, 앱 내 또는 앱 간의 작업 상태를 안정적으로 찾을 수 있습니다.
>




**When it’s feasible, let people halt processing.** If people can interrupt a process without causing negative side effects, include a Cancel button. If interrupting the process might cause negative side effects — such as losing the downloaded portion of a file — it can be useful to provide a Pause button in addition to a Cancel button.
> 가능하면 사람들이 처리를 중단하도록 하고, 사람들이 부정적인 부작용을 일으키지 않고 프로세스를 중단할 수 있다면 취소 버튼을 포함합니다. 프로세스를 중단하면 파일의 다운로드된 부분이 손실되는 등 부정적인 부작용이 발생할 수 있는 경우 취소 단추 외에 일시 중지 단추를 제공하는 것이 유용할 수 있습니다.
>




**Let people know when halting a process has a negative consequence.**When canceling a process results in lost progress, it’s helpful to provide an [alert](../components/presentation/alerts) with an an option to confirm the cancellation or resume the process.
> 프로세스를 중지하면 부정적인 결과가 발생한다는 것을 사람들에게 알립니다.프로세스를 취소하면 진행률이 손실되는 경우 취소를 확인하거나 프로세스를 다시 시작하는 옵션과 함께 알림을 제공하는 것이 유용합니다.
>




# **Platform considerations**

*No additional considerations for tvOS or watchOS.*
> TVOS 또는 시계에 대한 추가 고려 사항 없음운영 체제
>




# **iOS, iPadOS**

Progress indicators have two distinct styles.
> 진행률 표시기에는 두 가지 다른 스타일이 있습니다.
>




*Progress bars* include a track that fills from the leading side to the trailing side to show the progression of a task. Progress bars are always determinate in iOS and iPadOS. For developer guidance, see [UIProgressView](https://developer.apple.com/documentation/uikit/uiprogressview).
> 진행률 표시줄에는 작업의 진행률을 표시하기 위해 선행 측에서 후행 측으로 채워지는 트랙이 포함됩니다. iOS와 iPadOS에서는 진행률 표시줄이 항상 결정됩니다. 개발자 지침은 UIProgressView를 참조하십시오.
>




![https://developer.apple.com/design/human-interface-guidelines/components/status/progress-indicators/images/progress-bar_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/status/progress-indicators/images/progress-bar_2x.png)

Play

*Activity indicators* spin while a task is performed. Activity indicators are always indeterminate in iOS and iPadOS. For developer guidance, see [UIActivityIndicatorView](https://developer.apple.com/documentation/uikit/uiactivityindicatorview).
> 작업이 수행되는 동안 활동 표시기가 회전합니다. iOS와 아이패드OS에서 활동 지표는 항상 불확실하다. 개발자 지침은 UIActivity를 참조하십시오.표시기 보기.
>




![https://developer.apple.com/design/human-interface-guidelines/components/status/progress-indicators/images/activity-indicators_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/status/progress-indicators/images/activity-indicators_2x.png)

Play

**Hide the unfilled portion of the track in navigation bars and toolbars.**By default, a progress bar’s track includes both filled and unfilled portions. When you use a progress bar in a navigation bar or toolbar — for example, to show a page loading — configure it to hide the unfilled portion of the track.
> 탐색 모음 및 도구 모음에서 트랙의 채워지지 않은 부분을 숨깁니다.기본적으로 진행 표시줄의 트랙에는 채워진 부분과 채워지지 않은 부분이 모두 포함됩니다. 페이지 로드를 표시하기 위해 탐색 모음이나 도구 모음에서 진행률 표시줄을 사용할 때 트랙의 채워지지 않은 부분을 숨기도록 구성합니다.
>




### **Refresh content controls**

A refresh control is manually initiated to immediately reload content, typically in a table view, without waiting for the next automatic content update to occur. A refresh control is a specialized type of activity indicator, is hidden by default, and becomes visible when dragging down on the view to be reloaded. In Mail, for example, you can drag the list of Inbox messages down to check for new messages.
> 새로 고침 컨트롤은 다음 자동 내용 업데이트가 발생할 때까지 기다리지 않고 일반적으로 테이블 보기에서 내용을 즉시 다시 로드하기 위해 수동으로 시작됩니다. 새로 고침 컨트롤은 작업 표시기의 특수한 유형으로, 기본적으로 숨겨져 있으며 다시 로드할 보기에서 아래로 끌면 표시됩니다. 예를 들어, 메일에서 받은 문서 메시지 목록을 아래로 끌어 새 메시지를 확인할 수 있습니다.
>




![https://developer.apple.com/design/human-interface-guidelines/components/status/progress-indicators/images/refresh-controls_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/status/progress-indicators/images/refresh-controls_2x.png)

Play

**Perform automatic content updates.** Although people appreciate being able to trigger an immediate content refresh, they also expect automatic refreshes to occur periodically. Don’t make people responsible for initiating every update. Keep data fresh by updating it regularly.
> 자동 콘텐츠 업데이트를 수행합니다. 사람들은 즉시 콘텐츠 새로 고침을 트리거할 수 있는 것을 높이 평가하지만, 자동 새로 고침이 주기적으로 발생할 것으로 예상합니다. 모든 업데이트를 시작할 책임이 있는 사용자를 만들지 마십시오. 정기적으로 데이터를 업데이트하여 최신 상태로 유지합니다.
>




**Supply a short title only if it adds value.** Optionally, a refresh control can include a title. In most cases, this is unnecessary, as the animation of the control indicates that content is loading. If you do include a title, don’t use it to explain how to perform a refresh. Instead, provide information of value about the content being refreshed. A refresh control in Podcasts, for example, uses a title to tell people when the last podcast update occurred.
> 값을 추가하는 경우에만 짧은 제목을 지정하십시오. 선택적으로 새로 고침 컨트롤에 제목이 포함될 수 있습니다. 대부분의 경우 컨트롤의 애니메이션에 콘텐츠가 로드되고 있음이 표시되므로 이 작업은 필요하지 않습니다. 제목이 포함된 경우 새로 고침을 수행하는 방법을 설명하는 데 사용하지 마십시오. 대신 새로 고칠 내용에 대한 유용한 정보를 제공하십시오. 예를 들어 팟캐스트의 새로 고침 컨트롤은 제목을 사용하여 마지막 팟캐스트 업데이트가 발생한 시간을 알려줍니다.
>




For developer guidance, see [UIRefreshControl](https://developer.apple.com/documentation/uikit/uirefreshcontrol).

# **macOS**

Progress indicators have two distinct styles, each with a determinate and an indeterminate type.
> 진행률 표시기에는 두 가지 다른 스타일이 있으며, 각각 결정형과 불확정형이 있습니다.
>




*Bar indicators*, also known as *progress bars*, show progress in a horizontal bar. Determinate bar indicators fill from the leading side to the trailing side, while indeterminate indicators have an animated pulse. For developer guidance, see [NSProgressIndicatorBarStyle](https://developer.apple.com/documentation/appkit/nsprogressindicatorstylebar).
> 진행률 표시줄이라고도 하는 막대 표시기는 수평 막대에서 진행률을 표시합니다. 선행 측에서 후행 측으로 채워지는 막대 표시기를 결정하고, 불확정 측 표시기에는 애니메이션 펄스가 있습니다. 개발자 지침은 NSProgress를 참조하십시오.표시 막대 스타일.
>




![https://developer.apple.com/design/human-interface-guidelines/components/status/progress-indicators/images/progress-indicator-determinate-bar_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/status/progress-indicators/images/progress-indicator-determinate-bar_2x.png)

Determinate progress bar

![https://developer.apple.com/design/human-interface-guidelines/components/status/progress-indicators/images/progress-indicator-determinate-circle_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/status/progress-indicators/images/progress-indicator-determinate-circle_2x.png)

Determinate progress circle

*Spinning indicators*, also known as *spinners,* show progress in a circular form. Determinate spinning indicators are circles that fill in as progress continues, while indeterminate indicators have a rotating animation. For developer guidance, see [NSProgressIndicatorSpinningStyle](https://developer.apple.com/documentation/appkit/nsprogressindicatorspinningstyle).
> 스피너(spinner)라고도 하는 스피닝 인디케이터는 원형으로 진행을 보여준다. 결정 회전 표시기는 진행이 계속됨에 따라 채워지는 원이며, 반면 불확정 표시기는 회전 애니메이션을 가지고 있습니다. 개발자 지침은 NSProgress를 참조하십시오.지시자 회전 스타일.
>




![https://developer.apple.com/design/human-interface-guidelines/components/status/progress-indicators/images/progress-indicator-intermediate-bar_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/status/progress-indicators/images/progress-indicator-intermediate-bar_2x.png)

Indeterminate progress bar

![https://developer.apple.com/design/human-interface-guidelines/components/status/progress-indicators/images/progress-indicator-intermediate-spinner_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/status/progress-indicators/images/progress-indicator-intermediate-spinner_2x.png)

Spinning progress indicator

**Prefer a spinning progress indicator to communicate the status of a background operation or when space is constrained.** Spinners are small and unobtrusive, so they’re useful for asynchronous background tasks, like retrieving messages from a server. Spinners are also good for communicating progress within a small area, such as within a text field or next to a specific control, such as a button.
> 회전 진행률 표시기는 백그라운드 작업의 상태를 전달하거나 공간이 제한될 때 사용합니다. 회전 속도 표시기는 작고 눈에 띄지 않으므로 서버에서 메시지를 검색하는 것과 같은 비동기 백그라운드 작업에 유용합니다. 스피너는 또한 텍스트 필드 내 또는 버튼과 같은 특정 컨트롤 옆과 같은 작은 영역 내에서 진행 상황을 전달하는 데 유용합니다.
>




**Avoid labeling a spinning progress indicator.** Because a spinner typically appears when people initiate a process, a label is usually unnecessary.
> 회전 진행 표시기에 레이블을 지정하지 마십시오. 일반적으로 사람이 프로세스를 시작할 때 스피너가 나타나기 때문에 레이블이 필요하지 않습니다.
>



