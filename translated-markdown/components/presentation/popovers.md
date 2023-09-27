# **[components-presentation] popovers**

## A popover is a transient view that appears above other content onscreen when people click or tap a control or interactive area.
> 팝업은 사용자가 컨트롤 또는 대화형 영역을 클릭하거나 누를 때 화면의 다른 콘텐츠 위에 나타나는 일시적인 보기입니다.
>




![https://developer.apple.com/design/human-interface-guidelines/images/intro/components/popover-intro-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/components/popover-intro-dark_2x.png)

# **Best practices**

**Use a popover to expose a small amount of information or functionality.**Because a popover disappears after people interact with it, limit the amount of functionality in the popover to a few related tasks. For example, a calendar event popover makes it easy for people to change the date or time of an event, or to move it to another calendar. The popover disappears after the change, letting people continue reviewing the events on their calendar.
> 팝업을 사용하여 적은 양의 정보 또는 기능을 표시합니다.팝업은 사용자가 상호 작용한 후 사라지므로 팝업의 기능 양을 몇 가지 관련 작업으로 제한하십시오. 예를 들어, 일정관리 이벤트 팝업을 사용하면 이벤트의 날짜 또는 시간을 쉽게 변경하거나 다른 일정관리로 이동할 수 있습니다. 변경 후 팝업은 사라지며, 사람들은 달력에서 이벤트를 계속 검토할 수 있습니다.
>




**Consider using popovers when you want more room for content.** Views like sidebars and panels take up a lot of space. If you need content only temporarily, displaying it in a popover can help streamline your interface.
> 내용을 저장할 공간이 더 필요할 때는 팝업을 사용하는 것을 고려하십시오. 사이드바와 패널과 같은 보기는 많은 공간을 차지합니다. 콘텐츠가 일시적으로만 필요한 경우 팝업으로 표시하면 인터페이스를 간소화하는 데 도움이 됩니다.
>




**Position popovers appropriately onscreen.** Make sure a popover’s arrow points as directly as possible to the element that revealed it. Ideally, a popover doesn’t cover the element that revealed it or any essential content people may need to see while using it.
> 화면에 팝오버를 적절하게 배치합니다. 팝오버의 화살표가 가능한 한 노출된 요소를 직접 가리키는지 확인하십시오. 이상적으로, 팝오버는 그것을 드러낸 요소나 사람들이 그것을 사용하는 동안 봐야 할 필수적인 내용을 다루지 않는다.
>




**Use a Close button for confirmation and guidance only.** A Close button, including Cancel or Done, is worth including if it provides clarity, like exiting with or without saving changes. Otherwise, a popover generally closes when people click or tap outside its bounds or select an item in the popover. If multiple selections are possible, make sure the popover remains open until people explicitly dismiss it or they click or tap outside its bounds.
> 확인 및 안내를 위해서만 Close(닫기) 버튼을 사용하십시오. Cancel(취소) 또는 Done(완료)을 포함한 Close(닫기) 버튼은 변경 내용을 저장하거나 저장하지 않고 종료하는 것과 같은 명확한 정보를 제공하는 경우 포함할 가치가 있습니다. 그렇지 않으면 일반적으로 사람들이 범위 밖에서 클릭하거나 탭하거나 팝업에서 항목을 선택할 때 팝업이 닫힙니다. 여러 개를 선택할 수 있는 경우, 사람들이 팝오버를 명시적으로 해제하거나, 클릭하거나 탭을 할 때까지 팝오버가 열려 있는지 확인하십시오.
>




**Always save work when automatically closing a nonmodal popover.**People can unintentionally dismiss a nonmodal popover by clicking or tapping another part of the screen. Discard work only when people click or tap an explicit Cancel button.
> 비모달 팝업을 자동으로 닫을 때는 항상 작업을 저장하십시오.사람들은 화면의 다른 부분을 클릭하거나 탭함으로써 의도치 않게 비모달 팝오버를 해제할 수 있다. 사용자가 명시적인 취소 단추를 누르거나 누를 때만 작업을 취소합니다.
>




**Show one popover at a time.** Displaying multiple popovers clutters the interface and causes confusion. Never show a cascade or hierarchy of popovers, in which one emerges from another. If you need to show a new popover, close the open one first.
> 한 번에 하나의 팝업을 표시합니다. 여러 개의 팝업을 표시하면 인터페이스가 복잡해지고 혼동이 발생합니다. 하나가 다른 것에서 나오는, 절대로 계단식이나 팝오버 계층을 보여주지 마세요. 새 팝업을 표시하려면 열려 있는 팝업을 먼저 닫으십시오.
>




**Don’t show another view over a popover.** Make sure nothing displays on top of a popover, except for an alert.
> 팝업 창에 다른 보기를 표시하지 마십시오. 팝업 창 위에 경고를 제외하고 아무 것도 표시되지 않도록 하십시오.
>




**When possible, let people close one popover and open another with a single click or tap.** Avoiding extra gestures is especially desirable when several different bar buttons each open a popover.
> 가능하면 한 번의 클릭이나 탭으로 사람들이 하나의 팝업을 닫고 다른 팝업을 열도록 합니다. 여러 개의 다른 막대 단추가 각각 팝업을 열 때 추가 제스처를 피하는 것이 특히 좋습니다.
>




**Avoid making a popover too big.** Make a popover only big enough to display its contents and point to the place it came from — rather than take over the entire screen. Be aware that the system might adjust the size of a popover to ensure it fits well onscreen.
> 팝업을 너무 크게 만들지 않도록 합니다. 팝업을 전체 화면을 표시하는 대신 내용을 표시하고 원래 위치를 가리킬 수 있을 정도로만 만듭니다. 팝업이 화면에 잘 맞도록 시스템이 팝업 크기를 조정할 수 있습니다.
>




**Provide a smooth transition when changing the size of a popover.** Some popovers provide both condensed and expanded views of the same information. If you adjust the size of a popover, animate the change to avoid giving the impression that a new popover replaced the old one.
> 팝업의 크기를 변경할 때 원활한 전환을 제공합니다. 일부 팝업은 동일한 정보의 요약 보기와 확장 보기를 모두 제공합니다. 팝오버의 크기를 조정하는 경우 새 팝오버가 이전 팝오버를 대체했다는 인상을 주지 않도록 변경 내용을 애니메이션으로 표시합니다.
>




**Avoid using the word *popover* in help documentation.** Instead, refer to a specific task or selection. For example, instead of “Select the Show button at the bottom of the popover,” you might write “Select the Show button.”
> 도움말 설명서에서 popover라는 단어를 사용하지 않도록 합니다. 대신 특정 작업 또는 선택 항목을 참조하십시오. 예를 들어, "팝오버 하단의 표시 단추 선택" 대신 "표시 단추 선택"을 쓸 수 있습니다.
>




**Avoid using a popover to show a warning.** People can easily or accidentally dismiss popovers. Use [alerts](../components/presentation/alerts) to warn people instead.
> 경고를 표시하기 위해 팝오버를 사용하지 마십시오. 사람들은 팝오버를 쉽게 또는 실수로 무시할 수 있습니다. 대신 경보를 사용하여 사람들에게 경고합니다.
>




# **Platform considerations**

*Not supported in tvOS or watchOS.*
> TVOS 또는 워치에서 지원되지 않음운영 체제
>




# **iOS, iPadOS**

**Avoid displaying popovers in compact views.** Make your app or game dynamically adjust its layout based on the size class of the content area. Reserve popovers for wide views; for compact views, use all available screen space by presenting information in a full-screen modal view like a sheet instead. For related guidance, see [Modality](../ios/app-architecture/modality/).
> 앱이나 게임이 콘텐츠 영역의 크기 클래스에 따라 레이아웃을 동적으로 조정하도록 합니다. 넓은 보기를 위해 팝오버를 예약하고, 컴팩트 보기를 위해 대신 시트와 같은 전체 화면 모달 보기로 정보를 표시하여 사용 가능한 모든 화면 공간을 사용합니다. 관련 지침은 촬영장비를 참조하십시오.
>




# **macOS**

You can make a popover detachable in macOS, which becomes a separate panel when people drag it. The panel remains visible onscreen while people interact with other content.
> 사람이 끌면 별도의 패널이 되는 macOS에서 팝오버를 분리할 수 있습니다. 패널은 사용자가 다른 콘텐츠와 상호 작용하는 동안 화면에 표시됩니다.
>




![https://developer.apple.com/design/human-interface-guidelines/components/presentation/popovers/images/detached-popover_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/presentation/popovers/images/detached-popover_2x.png)

**Consider letting people detach a popover.** People might appreciate being able to convert a popover into a panel if they want to view other information while the popover remains visible.
> 팝업이 표시된 상태에서 다른 정보를 보려면 팝업을 패널로 변환할 수 있습니다.
>




**Make minimal appearance changes to a detached popover.** A panel that looks similar to the original popover helps people maintain context.
> 분리된 팝업을 최소한으로 변경합니다. 원래 팝업과 비슷하게 생긴 패널은 사람들이 상황을 유지하는 데 도움이 됩니다.
>



