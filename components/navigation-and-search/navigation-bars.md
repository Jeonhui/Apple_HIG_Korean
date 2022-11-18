# **[components-navigation-and-search] navigation-bars**

## A navigation bar appears at the top of an app screen, enabling navigation through a hierarchy of content.
> 앱 화면 상단에 탐색 모음이 나타나 콘텐츠 계층을 탐색할 수 있습니다.
>




![https://developer.apple.com/design/human-interface-guidelines/images/intro/components/navigation-bar-intro-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/components/navigation-bar-intro-dark_2x.png)

A navigation bar also provides a natural place to display a screen’s title — helping people orient themselves in your app or game — and it can include controls that affect the screen’s content.
> 탐색 모음은 또한 화면 제목을 자연스럽게 표시할 수 있는 위치를 제공하여 사람들이 앱이나 게임에서 방향을 지정할 수 있도록 도와주며, 화면 내용에 영향을 미치는 컨트롤을 포함할 수 있습니다.
>




macOS doesn’t provide a navigation bar. To enable navigation in a macOS app, you often use a [sidebar](../components/navigation-and-search/sidebars) or a navigation control like a Back button in a [toolbar](../components/menus-and-actions/toolbars). Also, you typically display the title of a macOS [window](../components/presentation/windows) in the title bar.
> macOS는 탐색 모음을 제공하지 않습니다. MacOS 앱에서 탐색을 사용하려면 도구 모음의 뒤로 단추와 같은 사이드바나 탐색 컨트롤을 사용하는 경우가 많습니다. 또한 일반적으로 제목 표시줄에 macOS 창의 제목을 표시합니다.
>




# **Best practices**

**Use the title area to describe the current screen if it provides useful context.** A screen’s title helps people confirm their location as they navigate your app. However, if titling a navigation bar seems redundant, you can leave the title area empty. For example, Notes doesn’t title the current note because the first line of content typically supplies sufficient context. Your app’s name doesn’t provide useful information about the screen or your content hierarchy, so it doesn’t work well as a title.
> 유용한 컨텍스트를 제공하는 경우 제목 영역을 사용하여 현재 화면을 설명합니다. 화면 제목은 사용자가 앱을 탐색할 때 자신의 위치를 확인하는 데 도움이 됩니다. 그러나 탐색 모음 제목이 중복되는 경우 제목 영역을 비워 둘 수 있습니다. 예를 들어, 일반적으로 내용의 첫 줄이 충분한 컨텍스트를 제공하므로 Notes는 현재 노트의 제목을 지정하지 않습니다. 앱 이름은 화면 또는 콘텐츠 계층에 대한 유용한 정보를 제공하지 않으므로 제목으로 제대로 작동하지 않습니다.
>




**Write a concise screen title.** Aim for a word or short phrase that distills the purpose of the screen. Using no more than about 15 characters tends to work well in most screens because it leaves enough room for a back button and optional controls.
> 간결한 화면 제목을 작성합니다. 화면의 목적을 증류하는 단어나 짧은 문구를 목표로 합니다. 약 15자 이하의 문자를 사용하는 것은 뒤로 버튼과 옵션 컨트롤을 위한 충분한 공간을 남기기 때문에 대부분의 화면에서 잘 작동하는 경향이 있다.
>




**Consider temporarily hiding the navigation bar to provide a more immersive experience.** For example, Photos hides the navigation bar and other interface elements when people view full-screen photos. If you implement this type of behavior, let people restore the navigation bar by tapping the screen or swiping down.
> 사람들이 전체 화면 사진을 볼 때 사진은 탐색 모음 및 기타 인터페이스 요소를 숨깁니다. 이러한 유형의 동작을 구현하는 경우 화면을 누르거나 아래로 쓸어내려서 탐색 모음을 복원할 수 있습니다.
>




**Use the standard back button.** People know that the standard back button lets them retrace their steps through a hierarchy of information. If you implement a custom back button, make sure it still looks like a back button, behaves as people expect, matches the rest of your interface, and is consistently implemented throughout your app or game. If you replace the system-provided back button chevron with a custom image, you may need to supply a custom mask image, too. For example, iOS uses this mask to animate the button title during transitions.
> 표준 뒤로 버튼을 사용합니다. 사람들은 표준 뒤로 버튼을 사용하면 정보의 계층을 통해 자신의 단계를 다시 추적할 수 있다는 것을 알고 있습니다. 사용자 지정 뒤로 버튼을 구현하는 경우, 여전히 뒤로 버튼처럼 보이고, 사람들이 예상하는 대로 작동하며, 인터페이스의 나머지 부분과 일치하며, 앱이나 게임 전반에 걸쳐 일관되게 구현되는지 확인하십시오. 시스템에서 제공하는 백 버튼 쉐브론을 사용자 지정 이미지로 교체하는 경우 사용자 지정 마스크 이미지도 제공해야 할 수 있습니다. 예를 들어 iOS는 전환 중에 버튼 제목을 애니메이션화하기 위해 이 마스크를 사용합니다.
>




**Make sure buttons that use text labels have enough room.** If your navigation bar includes more than one text-labeled button, the text of those buttons may appear to run together, making the buttons indistinguishable. Add separation by inserting a fixed-space item between the buttons. For developer guidance, see [UIBarButtonSystemItemFixedSpace](https://developer.apple.com/documentation/uikit/uibarbuttonsystemitem/uibarbuttonsystemitemfixedspace).
> 텍스트 레이블을 사용하는 단추에 충분한 공간이 있는지 확인하십시오. 탐색 모음에 텍스트 레이블이 있는 단추가 두 개 이상 포함되어 있으면 해당 단추의 텍스트가 함께 실행되어 단추를 구분하지 못하는 것처럼 보일 수 있습니다. 버튼 사이에 고정 공간 항목을 삽입하여 분리를 추가합니다. 개발자 지침은 UIBarButtonSystemItemFixedSpace를 참조하십시오.
>




# **Platform considerations**

*No additional considerations for tvOS. Not supported in macOS.*
> TVOS에 대한 추가 고려 사항은 없습니다. macOS에서는 지원되지 않습니다.
>




# **iOS, iPadOS**

**Consider using a segmented control in a navigation bar to flatten the information hierarchy.** For example, Phone uses a segmented control in the navigation bar of the Recents tab to let people switch between viewing all recent calls or only missed ones. If a design like this makes sense in your app, place a segmented control in the navigation bar only at the top level of the hierarchy, and be sure to create accurate back-button labels for the second-level screens. For guidance, see [Segmented controls](../components/selection-and-input/segmented-controls).
> 예를 들어 최근 탭의 탐색 모음에 있는 세그먼트 컨트롤을 사용하여 최근 통화를 모두 보거나 놓친 통화만 볼 수 있습니다. 앱에서 이와 같은 디자인이 타당하다면 계층의 최상위 수준에서만 탐색 모음에 세그먼트화된 컨트롤을 배치하고 2단계 화면에 대한 정확한 백 버튼 레이블을 만들어야 합니다. 자세한 내용은 세그먼트 컨트롤을 참조하십시오.
>




**Use a large title to help people stay oriented as they navigate and scroll.** For example, Phone uses the large title to clarify the active tab, while Music uses large titles to differentiate content areas like albums, artists, playlists, and radio. By default, a large title transitions to a standard title as people begin scrolling the content, and transitions back to large when people scroll to the top, reminding them of their current location. For developer guidance, see [prefersLargeTitles](https://developer.apple.com/documentation/uikit/uinavigationbar/2908999-preferslargetitles).
> 예를 들어 전화기는 활성 탭을 명확히 하기 위해 큰 제목을 사용하는 반면 음악은 앨범, 아티스트, 재생 목록 및 라디오와 같은 콘텐츠 영역을 구분하기 위해 큰 제목을 사용합니다. 기본적으로 큰 제목은 사용자가 내용을 스크롤하기 시작할 때 표준 제목으로 전환되고, 사용자가 현재 위치를 알려주면서 맨 위로 스크롤할 때 다시 큰 제목으로 전환됩니다. 개발자 지침은 큰 제목 선호를 참조하십시오.
>




![https://developer.apple.com/design/human-interface-guidelines/ios/images/NavigationBar_Standard_2x.png](https://developer.apple.com/design/human-interface-guidelines/ios/images/NavigationBar_Standard_2x.png)

Standard title

![https://developer.apple.com/design/human-interface-guidelines/ios/images/NavigationBar_Large_2x.png](https://developer.apple.com/design/human-interface-guidelines/ios/images/NavigationBar_Large_2x.png)

Large title

**Consider hiding the border of a large-title navigation bar to enhance the sense of connection between title and content.** Use caution applying this design to a standard-title navigation bar, though, because the bar’s title and buttons might be harder to distinguish without a visible border. In contrast, you might want to maintain consistency between the primary and secondary views in a Split View on iPad by using the borderless style in both. You can hide the bottom border of a navigation bar by removing the bar’s shadow (the border automatically reappears when people scroll the content area).
> 제목과 내용 사이의 연결을 향상시키기 위해 큰 제목의 탐색 모음의 테두리를 숨기는 것을 고려해 보십시오. 그러나 표시줄의 제목과 단추는 테두리가 보이지 않으면 구분하기 어려울 수 있으므로 표준 제목의 탐색 모음에 이 설계를 적용할 때 주의하십시오. 반대로 iPad의 분할 보기에서 테두리 없는 스타일을 사용하여 기본 보기와 보조 보기 간의 일관성을 유지할 수 있습니다. 막대의 그림자를 제거하여 탐색 막대의 아래쪽 테두리를 숨길 수 있습니다. 내용 영역을 스크롤할 때 테두리가 자동으로 다시 나타납니다.
>




# **watchOS**

The navigation bar appears at the top edge of the Apple Watch screen. The system offers space for a title in the leading end of the navigation bar and displays the clock in the trailing end.
> 탐색 모음은 Apple Watch 화면의 상단 가장자리에 나타납니다. 시스템은 탐색 모음의 앞쪽 끝에 제목을 위한 공간을 제공하고 뒤쪽 끝에 시계를 표시합니다.
>




The title area can include navigational elements in two cases.
> 제목 영역은 두 가지 경우에 탐색 요소를 포함할 수 있다.
>




An app that uses hierarchical navigation displays a back button next to the title of a detail screen. You can’t customize the back button icon.
> 계층 탐색을 사용하는 앱은 세부 화면 제목 옆에 뒤로 단추를 표시합니다. 뒤로 단추 아이콘은 사용자 지정할 수 없습니다.
>




![https://developer.apple.com/design/human-interface-guidelines/watchos/images/status-bar_hierarchical-ui_2x.png](https://developer.apple.com/design/human-interface-guidelines/watchos/images/status-bar_hierarchical-ui_2x.png)

In a modal sheet, the system covers the clock and displays the button that dismisses the sheet in the title area.
> 모달 시트에서 시스템은 시계를 덮고 제목 영역에 시트를 해제하는 버튼을 표시합니다.
>




![https://developer.apple.com/design/human-interface-guidelines/watchos/images/status-bar-modal-sheet_2x.png](https://developer.apple.com/design/human-interface-guidelines/watchos/images/status-bar-modal-sheet_2x.png)

**IMPORTANT**The clock appears in the navigation bar of every nonmodal app screen. You can’t remove the clock, so be sure to account for it in your designs.
> 중요 시계는 모든 비모달 앱 화면의 탐색 표시줄에 표시됩니다. 시계는 제거할 수 없으므로 설계 시 반드시 고려해야 합니다.
>




The system uses the minimum layout margins to inset both your title and the clock from the edges of the screen, particularly on Apple Watch Series 4 and later (shown below). For guidance, see [Layout](../foundations/layout).
> 시스템은 최소 레이아웃 여백을 사용하여 특히 Apple Watch Series 4 이상(아래 표시)에서 화면 가장자리에서 제목과 시계를 모두 삽입합니다. 자세한 내용은 레이아웃을 참조하십시오.
>




![https://developer.apple.com/design/human-interface-guidelines/watchos/images/status-bar-guides_2x.png](https://developer.apple.com/design/human-interface-guidelines/watchos/images/status-bar-guides_2x.png)
