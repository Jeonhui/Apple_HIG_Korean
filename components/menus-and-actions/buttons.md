# **[components-menus-and-actions] buttons**

## A button initiates an instantaneous action.
> 버튼을 누르면 순간적인 동작이 시작됩니다.
>




![https://developer.apple.com/design/human-interface-guidelines/images/intro/components/buttons-intro-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/components/buttons-intro-dark_2x.png)

Versatile and highly customizable, buttons give people simple, familiar ways to do tasks in your app. In general, a button combines three attributes to clearly communicate its function:
> 다재다능하고 사용자 지정이 가능한 버튼은 앱에서 작업을 수행하는 간단하고 친숙한 방법을 제공합니다. 일반적으로 버튼은 기능을 명확하게 전달하기 위해 세 가지 속성을 결합합니다.
>




- **Style.** A visual style based on size, color, and shape.
- >  스타일. 크기, 색상 및 모양을 기반으로 한 시각적 스타일입니다.

- **Content.** The symbol (or interface icon), text label, or both that a button displays to convey its purpose.
- >  내용. 단추가 목적을 전달하기 위해 표시하는 기호(또는 인터페이스 아이콘), 텍스트 레이블 또는 둘 다입니다.

- **Role.** A system-defined role that identifies a button’s semantic meaning and can affect its appearance.
- >  역할. 버튼의 의미적 의미를 식별하고 버튼의 모양에 영향을 줄 수 있는 시스템 정의 역할입니다.


In addition to all-purpose buttons, many common button styles — like Info, Close, and Contact Add — enable familiar behaviors throughout the system. There are also many button-like components that have distinct appearances and behaviors for specific use cases, like [toggles](../components/selection-and-input/toggles), [pop-up buttons](../components/menus-and-actions/pop-up-buttons), and [segmented controls](../components/selection-and-input/segmented-controls).
> 다목적 버튼 외에도 정보, 닫기 및 연락처 추가와 같은 많은 일반적인 버튼 스타일을 통해 시스템 전체에서 익숙한 동작을 수행할 수 있습니다. 또한 토글, 팝업 버튼 및 세그먼트 조정기와 같은 특정 사용 사례에 대해 뚜렷한 모양과 동작을 갖는 버튼과 같은 구성 요소가 많이 있다.
>




# **Best practices**

When buttons are instantly recognizable and easy to understand, an app tends to feel intuitive and well designed.
> 버튼을 즉시 인식할 수 있고 이해하기 쉬울 때, 앱은 직관적이고 잘 디자인된 것처럼 느끼는 경향이 있다.
>




**Make buttons easy for people to choose.** On a touchscreen, buttons need a hit target of at least 44x44 points to accommodate a fingertip. On all screens, it’s essential to include enough space around a button so that people can visually distinguish it from surrounding components and content, whether people use touch, a pointer, or a system that expands a button when it’s in focus.
> 터치스크린에서 버튼은 손가락 끝을 수용하기 위해 최소 44x44 포인트의 적중 대상이 필요하다. 모든 화면에서 버튼 주위에 충분한 공간을 포함시켜 사람들이 터치, 포인터, 또는 초점이 맞춰졌을 때 버튼을 확장하는 시스템 등 주변 구성 요소 및 콘텐츠와 시각적으로 구별할 수 있도록 하는 것이 필수적이다.
>




**Ensure that each button clearly communicates it purpose.** A button always includes a text label or a symbol (or interface icon) — and sometimes a combination of both — to help people predict what it does.
> 각 단추가 목적을 명확하게 전달하는지 확인하십시오. 단추에는 항상 텍스트 레이블이나 기호(또는 인터페이스 아이콘)가 포함되며, 때로는 이 두 개의 조합이 포함되어 있어 사용자가 무엇을 하는지 예측할 수 있습니다.
>




# **Style**

System buttons offer a range of styles that support extensive customization while providing built-in interaction states, accessibility support, and appearance adaptation.
> 시스템 버튼은 광범위한 사용자 지정을 지원하는 동시에 내장된 상호 작용 상태, 접근성 지원 및 모양 적응을 제공하는 다양한 스타일을 제공합니다.
>




iOS and iPadOS have four button styles, each available in three sizes. Each combination of size and style has a different level of visual prominence, helping you present hierarchies of actions within your app.
> iOS 및 iPadOS에는 4개의 버튼 스타일이 있으며, 각 버튼은 3가지 크기로 제공됩니다. 크기와 스타일의 각 조합은 시각적 두드러짐의 다른 수준을 가지고 있어 앱 내에서 동작의 계층을 표시하는 데 도움이 됩니다.
>




![https://developer.apple.com/design/human-interface-guidelines/components/menus-and-actions/buttons/images/button-sizes-styles-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/menus-and-actions/buttons/images/button-sizes-styles-dark_2x.png)

You can configure a system button to use any combination of style and size. By default, a system button uses a size-specific corner radius and your app’s accent color. If necessary, you can change these attributes — in addition to attributes that control content layout and the presence of an activity indicator — in your button configuration.
> 스타일과 크기의 조합을 사용하도록 시스템 버튼을 구성할 수 있습니다. 기본적으로 시스템 버튼은 크기별 코너 반경과 앱의 악센트 색상을 사용합니다. 필요한 경우, 단추 구성에서 내용 레이아웃 및 활동 표시기의 존재를 제어하는 특성 외에도 이러한 특성을 변경할 수 있습니다.
>




**Use a filled button for the most likely action in a view.** The filled style is the most visually prominent, so it helps people quickly identify the action they’re most likely to want. At the same time, avoid using too many filled buttons in a view. Too many filled buttons can increase cognitive load because people must spend time comparing multiple likely options before making a choice.
> 보기에서 가장 가능성이 높은 작업을 수행하려면 채워진 단추를 사용하십시오. 채워진 스타일이 시각적으로 가장 두드러지므로 사용자가 가장 원하는 작업을 빠르게 식별할 수 있습니다. 동시에 보기에서 채워진 단추를 너무 많이 사용하지 않도록 합니다. 너무 많은 채워진 버튼은 사람들이 선택을 하기 전에 여러 가지 가능한 옵션을 비교하는 데 시간을 보내야 하기 때문에 인지 부하를 증가시킬 수 있다.
>




**Use style — not size — to visually distinguish the preferred choice among multiple options.** When you use buttons of the same size to offer two or more options, you signal that the options form a coherent set of choices. If you want to highlight the preferred or most likely option in a set, use a more prominent button style for that option and a less prominent style for the remaining ones.
> 크기가 아닌 스타일을 사용하여 여러 옵션 중에서 선호하는 항목을 시각적으로 구분합니다. 같은 크기의 단추를 사용하여 두 개 이상의 옵션을 제공하면 옵션이 일관된 선택 집합을 형성한다는 신호를 보냅니다. 세트에서 선호하거나 가장 가능성이 높은 옵션을 강조 표시하려면 해당 옵션에는 더 눈에 띄는 단추 스타일을 사용하고 나머지 옵션에는 덜 두드러지는 스타일을 사용하십시오.
>




# **Content**

**Create button content that helps people instantly understand what the button does.** If an interface icon makes sense in your button, consider using an existing or customized [SF Symbol](../sf-symbols/overview/). To use text, create a short label that succinctly describes what the button does. Using [title-style capitalization](https://help.apple.com/applestyleguide/#/apsgb744e4a3?sub=apdca93e113f1d64), consider starting the label with a verb to help convey the button’s action — for example, a button that lets people add items to their shopping cart might use the label “Add to Cart.”
> 단추의 기능을 즉시 이해할 수 있는 단추 콘텐츠를 만듭니다. 단추에 인터페이스 아이콘이 있으면 기존 또는 사용자 지정된 SF 기호를 사용하십시오. 텍스트를 사용하려면 단추의 기능을 간략하게 설명하는 짧은 레이블을 작성합니다. 예를 들어, 쇼핑 카트에 항목을 추가할 수 있는 단추는 "카트에 추가" 레이블을 사용할 수 있습니다.
>




**Include additional text below the label only if it provides useful details.**Additional text uses a smaller text size than the label, showing that the information is secondary to the button’s action. For example, you might add text to update an Add to Cart button with the number of items in the cart. Avoid writing a subtitle that explains more about what the button does; make sure a button’s containing view, label or image, style, and role provide all the information people need to understand its action.
> 유용한 세부 정보를 제공하는 경우에만 레이블 아래에 추가 텍스트를 포함하십시오.추가 텍스트는 레이블보다 더 작은 텍스트 크기를 사용하여 정보가 단추의 동작에 보조적이라는 것을 나타냅니다. 예를 들어 카트에 있는 항목 수로 카트에 추가 단추를 업데이트하기 위해 텍스트를 추가할 수 있습니다. 단추의 기능에 대해 자세히 설명하는 부제를 작성하지 마십시오. 단추의 보기, 레이블 또는 이미지, 스타일 및 역할이 사용자가 작업을 이해하는 데 필요한 모든 정보를 제공하는지 확인하십시오.
>




**Configure a button to display an activity indicator when you need to provide feedback about an action that doesn’t instantly complete.**Displaying an activity indicator within a button can save space in your user interface while clearly communicating the reason for the delay. To help clarify what’s happening, you can also configure the button to display a different label alongside the activity indicator. For example, the label “Checkout” could change to “Checking out...” while the activity indicator is visible. When a delay occurs after people click or tap your configured button, the system displays the activity indicator next to the original or alternative label, hiding the button image, if there is one.
> 즉시 완료되지 않은 작업에 대한 피드백을 제공해야 할 때 작업 표시기를 표시하는 단추를 구성합니다.단추 내에 활동 표시기를 표시하면 지연 이유를 명확하게 전달하면서 사용자 인터페이스의 공간을 절약할 수 있습니다. 또한 작업 표시기와 함께 다른 레이블을 표시하도록 단추를 구성할 수 있습니다. 예를 들어, 활동 표시기가 보이는 동안 "Checkout" 레이블이 "Checkout..."으로 변경될 수 있습니다. 사용자가 구성한 버튼을 클릭하거나 누른 후 지연이 발생하면 시스템은 원래 레이블 또는 대체 레이블 옆에 활동 표시기를 표시하고 단추 이미지가 있는 경우 이를 숨깁니다.
>




![https://developer.apple.com/design/human-interface-guidelines/components/menus-and-actions/buttons/images/button-activity-indicator-hidden_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/menus-and-actions/buttons/images/button-activity-indicator-hidden_2x.png)

![https://developer.apple.com/design/human-interface-guidelines/components/menus-and-actions/buttons/images/button-activity-indicator-visible_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/menus-and-actions/buttons/images/button-activity-indicator-visible_2x.png)

# **Role**

A system button can have one of the following roles:
> 시스템 버튼에는 다음 역할 중 하나가 포함될 수 있습니다.
>




- **Normal.** No specific meaning.
- **Primary.** The button is the default button — the button people are most likely to choose.
- >  기본. 단추는 기본 단추이며, 사용자가 가장 많이 선택하는 단추입니다.

- **Cancel.** The button cancels the current action.
- >  취소. 버튼을 누르면 현재 작업이 취소됩니다.

- **Destructive.** The button performs an action that can result in data destruction.
- >  파괴적입니다. 이 버튼은 데이터 파괴를 초래할 수 있는 작업을 수행합니다.


A button’s role can have additional effects on the appearance you configure. For example, the system uses bold text for the label in a primary button, whereas a destructive button uses a red color.
> 단추의 역할은 사용자가 구성한 모양에 추가 영향을 미칠 수 있습니다. 예를 들어, 시스템은 기본 단추의 레이블에 굵은 텍스트를 사용하는 반면, 파괴 단추는 빨간색 텍스트를 사용합니다.
>




**Assign the primary role to the button people are most likely to choose.**When a primary button responds to the Return key, it makes it easy for people to quickly confirm their choice. In addition, when the button is in a temporary view — like a [sheet](../components/presentation/sheets), an editable view, or an [alert](../components/presentation/alerts) — assigning it the primary role means that the view can automatically close when people press Return.
> 사용자가 가장 많이 선택할 수 있는 단추에 기본 역할을 할당합니다.기본 버튼이 Return 키에 응답하면, 사람들은 쉽게 그들의 선택을 확인할 수 있다. 또한 단추가 시트, 편집 가능한 보기 또는 알림과 같은 임시 보기에 있는 경우 기본 역할을 할당하면 사용자가 Return을 누를 때 보기가 자동으로 닫힐 수 있습니다.
>




**Don’t assign the primary role to a button that performs a destructive action, even if that action is the most likely choice.** Because of its visual prominence, people sometimes choose a primary button without reading it first. Help people avoid losing content by assigning the primary role to nondestructive buttons.
> 가장 유력한 선택일지라도 파괴적인 행동을 수행하는 단추에 주 역할을 할당하지 마십시오. 시각적 중요성 때문에 사람들은 주 단추를 먼저 읽지 않고 선택하는 경우가 있습니다. 주 역할을 비파괴 단추에 할당하여 사용자가 콘텐츠를 손실하지 않도록 합니다.
>




# **Platform considerations**

*No additional considerations for iOS, iPadOS, or tvOS.*
> iOS, iPadOS 또는 tvOS에 대한 추가 고려 사항 없음.
>




# **macOS**

Several specific button types are unique to macOS.
> 몇 가지 특정한 버튼 유형은 macOS에 고유합니다.
>




### **Push buttons**

The standard button type in macOS is known as a *push button*. You can configure a push button to display text, a symbol, an interface icon, or an image, or a combination of text and image content. Push buttons can act as the default button in a view and you can tint them.
> macOS에서 표준 버튼 유형은 푸시 버튼이라고 알려져 있습니다. 텍스트, 기호, 인터페이스 아이콘 또는 이미지를 표시하거나 텍스트와 이미지 내용의 조합을 표시하도록 푸시 버튼을 구성할 수 있습니다. 누름 단추는 보기에서 기본 단추 역할을 할 수 있으며 색조를 지정할 수 있습니다.
>




**Use a flexible-height push button only when you need to display tall or variable height content.** Flexible-height buttons support the same configurations as regular push buttons — and they use the same corner radius and content padding — so they look consistent with other buttons in your interface. If you need to present a button that contains two lines of text or a tall icon, use a flexible-height button; otherwise, use a standard push button. For developer guidance, see [NSBezelStyleRegularSquare](https://developer.apple.com/documentation/appkit/nsbezelstyle/nsbezelstyleregularsquare/).
> 높이 또는 높이 가변 콘텐츠를 표시해야 하는 경우에만 유연한 높이 푸시 버튼을 사용하십시오. 유연한 높이 버튼은 일반 푸시 버튼과 동일한 구성(코너 반경 및 내용 채우기 사용)을 지원하므로 인터페이스의 다른 버튼과 일관되게 보입니다. 두 줄의 텍스트나 큰 아이콘이 있는 단추를 표시해야 하는 경우 유연한 높이 단추를 사용하고 그렇지 않은 경우 표준 누름 단추를 사용합니다. 개발자 지침은 NSBezelStyle Regular Square를 참조하십시오.
>




**Append a trailing ellipsis to the title when a push button opens another window, view, or app.** Throughout the system, an ellipsis in a control title signals that people can provide additional input. For example, the Edit buttons in the AutoFill pane of Safari Settings include ellipses because they open other views that let people modify autofill values.
> 누름 버튼을 누르면 다른 창, 보기 또는 앱이 열릴 때 제목에 줄임표를 추가합니다. 시스템 전체에서 제어 제목 신호에 줄임표가 있어 사용자가 추가 입력을 제공할 수 있습니다. 예를 들어 Safari Settings의 AutoFill 창의 Edit(편집) 단추는 사람들이 자동 채우기 값을 수정할 수 있는 다른 보기를 열기 때문에 타원을 포함합니다.
>




**Consider enabling spring loading.** On systems with a Magic Trackpad, *spring loading* lets people activate a button by dragging selected items over it and force clicking — that is, pressing harder — without dropping the selected items. After force clicking, people can continue dragging the items, possibly to perform additional actions.
> 스프링 로드를 사용하도록 설정합니다. 매직 트랙패드가 있는 시스템에서는 스프링 로드를 사용하면 선택한 항목을 끌어다 놓고 선택한 항목을 삭제하지 않고 강제로 클릭(즉, 더 세게 누름)하여 버튼을 활성화할 수 있습니다. 강제 클릭 후 사용자는 항목을 계속 끌 수 있으며 추가 작업을 수행할 수도 있습니다.
>




### **Gradient buttons**

A gradient button initiates an action related to a view, like adding or removing rows in a table.
> 그라데이션 단추는 표의 행 추가 또는 제거와 같은 보기와 관련된 작업을 시작합니다.
>




![https://developer.apple.com/design/human-interface-guidelines/components/menus-and-actions/buttons/images/gradient-buttons-macos_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/menus-and-actions/buttons/images/gradient-buttons-macos_2x.png)

Gradient buttons contain symbols or interface icons — not text — and you can configure them to behave like push buttons, toggles, or pop-up buttons. The buttons appear in close proximity to their associated view — usually within or beneath it — so people know which view the buttons affect.
> 그라데이션 버튼에는 텍스트가 아닌 기호 또는 인터페이스 아이콘이 포함되어 있으며 푸시 버튼, 토글 또는 팝업 버튼처럼 동작하도록 구성할 수 있습니다. 단추는 일반적으로 단추 내부 또는 아래에 연결된 보기에 가깝게 나타나므로 단추가 어떤 보기에 영향을 미치는지 알 수 있습니다.
>




**Use gradient buttons in a view, not in the window frame.** Gradient buttons aren’t intended for use in toolbars or status bars. If you need a button in a [toolbar](../components/menus-and-actions/toolbars), use a toolbar item.
> 창 프레임이 아닌 보기에서 그라데이션 단추를 사용합니다. 그라데이션 단추는 도구 모음이나 상태 표시줄에서 사용할 수 없습니다. 도구 모음에 단추가 필요한 경우 도구 모음 항목을 사용하십시오.
>




**Prefer using a symbol in a gradient button.** [SF Symbols](../foundations/sf-symbols) provides a wide range of symbols that automatically receive appropriate coloring in their default state and in response to user interaction.
> 그라데이션 버튼에서 기호를 사용하는 것을 선호합니다. SF 심볼은 기본 상태에서 사용자 상호 작용에 따라 자동으로 적절한 색상을 받는 광범위한 기호를 제공합니다.
>




**Avoid using labels to introduce gradient buttons.** Because gradient buttons are closely connected with a specific view, their purpose is generally clear without the need for descriptive text.
> 그라데이션 버튼은 라벨 사용을 피한다. 그라데이션 버튼은 특정 뷰와 밀접하게 연결되어 있기 때문에 설명 텍스트 없이도 일반적으로 용도가 명확하다.
>




For developer guidance, see [NSBezelStyleSmallSquare](https://developer.apple.com/documentation/appkit/nsbezelstyle/nsbezelstylesmallsquare/).

### **Help buttons**

A help button appears within a view and opens app-specific help documentation.
> 도움말 버튼이 보기 내에 나타나고 앱별 도움말 문서를 엽니다.
>




![https://developer.apple.com/design/human-interface-guidelines/components/menus-and-actions/buttons/images/help-buttons-macos_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/menus-and-actions/buttons/images/help-buttons-macos_2x.png)

Help buttons are circular, consistently sized buttons that contain a question mark. For guidance on creating help documentation, see [Offering help](../patterns/offering-help).
> 도움말 버튼은 물음표가 포함된 일정한 크기의 원형 버튼입니다. 도움말 문서 작성에 대한 지침은 도움말 제공을 참조하십시오.
>




**Use the system-provided help button to display your help documentation.** People are familiar with the appearance of the standard help button and know that choosing it opens help content.
> 시스템 제공 도움말 단추를 사용하여 도움말 문서를 표시할 수 있습니다. 표준 도움말 단추의 모양에 익숙하고 이 단추를 선택하면 도움말 내용이 열린다는 것을 알고 있습니다.
>




**When possible, open the help topic that’s related to the current context.** For example, the help button in the Rules pane of Mail settings opens the Mail User Guide to a help topic that explains how to change these settings. If no specific help topic applies directly to the current context, open the top level of your app’s help documentation when people choose a help button.
> 가능한 경우 현재 컨텍스트와 관련된 도움말 항목을 엽니다. 예를 들어, 메일 설정 규칙 창의 도움말 단추는 이러한 설정을 변경하는 방법을 설명하는 도움말 항목으로 메일 사용자 안내서를 엽니다. 특정 도움말 항목이 현재 컨텍스트에 직접 적용되지 않는 경우, 사용자가 도움말 단추를 선택할 때 앱 도움말 문서의 최상위 단계를 여십시오.
>




**Include no more than one help button per window.** Multiple help buttons in the same context make it hard for people to predict the result of clicking one.
> 한 창당 도움말 단추를 하나만 포함하십시오. 동일한 컨텍스트에 있는 여러 개의 도움말 단추는 사용자가 한 개의 도움말 단추를 클릭하는 결과를 예측하기 어렵게 합니다.
>




**Position help buttons where people expect to find them.** Use the following locations for guidance.
> 도움말 버튼을 찾을 수 있는 위치에 놓으십시오. 안내를 위해 다음 위치를 사용하십시오.
>




| View style | Help button location |
| --- | --- |
| Dialog with dismissal buttons (like OK and Cancel) | Lower corner, opposite to the dismissal buttons and vertically aligned with them |
| Dialog without dismissal buttons | Lower-left or lower-right corner |
| Settings window or pane | Lower-left or lower-right corner |

**Use a help button within a view, not in the window frame.** For example, avoid placing a help button in a toolbar or status bar.
> 창 프레임이 아닌 보기 내에서 도움말 단추를 사용합니다. 예를 들어, 도구 모음이나 상태 표시줄에 도움말 단추를 배치하지 마십시오.
>




**Avoid displaying text that introduces a help button.** People know what a help button does, so they don’t need additional descriptive text.
> 도움말 단추가 포함된 텍스트를 표시하지 않도록 합니다. 도움말 단추의 기능을 알고 있으므로 추가 설명 텍스트가 필요하지 않습니다.
>




### **Image buttons**

An image button appears in a view and displays an image, symbol, or interface icon. You can configure an image button to behave like a push button, toggle, or pop-up button.
> 이미지 단추는 보기에 나타나고 이미지, 기호 또는 인터페이스 아이콘을 표시합니다. 누름 단추, 전환 단추 또는 팝업 단추처럼 동작하도록 이미지 단추를 구성할 수 있습니다.
>




![https://developer.apple.com/design/human-interface-guidelines/components/menus-and-actions/buttons/images/image-buttons-macos_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/menus-and-actions/buttons/images/image-buttons-macos_2x.png)

**Use an image button in a view, not in the window frame.** For example, avoid placing an image button in a toolbar or status bar. If you need to use an image as a button in a toolbar, use a toolbar item. See [Toolbars](../components/menus-and-actions/toolbars).
> 창 프레임이 아닌 보기에서 이미지 단추를 사용합니다. 예를 들어, 도구 모음이나 상태 표시줄에 이미지 단추를 배치하지 마십시오. 이미지를 도구 모음에서 단추로 사용해야 하는 경우 도구 모음 항목을 사용합니다. 도구 모음을 참조하십시오.
>




**Include about 10 pixels of padding between the edges of the image and the button edges.** An image button’s edges define its clickable area even when they aren’t visible. Including padding ensures that a click registers correctly even if it’s not precisely within the image. In general, avoid including a system-provided border in an image button; for developer guidance, see [isBordered](https://developer.apple.com/documentation/appkit/nsbutton/1525565-isbordered/).
> 이미지의 가장자리와 단추 가장자리 사이에 약 10픽셀의 패딩을 포함합니다. 이미지 단추의 가장자리는 보이지 않을 때에도 클릭 가능한 영역을 정의합니다. 패딩을 포함하면 클릭 한 번이 정확하게 이미지 내에 있지 않더라도 올바르게 등록됩니다. 일반적으로 이미지 단추에 시스템이 제공하는 테두리를 포함하지 마십시오. 개발자 지침은 경계선을 참조하십시오.
>




**If you need to include a label, position it below the image button.** For related guidance, see [Labels](../components/layout-and-organization/labels).
> 레이블을 포함해야 하는 경우 이미지 단추 아래에 레이블을 배치합니다. 관련 지침은 레이블을 참조하십시오.
>




# **watchOS**

**Prefer buttons that span the width of the screen.** Full-width buttons look better and are easier for people to tap. If two buttons must share the same horizontal space, use the same height for both, and use images or short text titles for each button’s content.
> 화면 너비에 걸쳐 있는 단추를 선택합니다. 전체 너비의 단추가 더 보기 좋고 사람들이 누르기 쉽습니다. 두 단추가 동일한 수평 공간을 공유해야 하는 경우 두 단추 모두에 동일한 높이를 사용하고 각 단추의 내용에 대해 이미지 또는 짧은 텍스트 제목을 사용합니다.
>




**Use the same height for vertical stacks of one- and two-line text buttons.** As much as possible, use identical button heights for visual consistency.
> 한 줄과 두 줄 텍스트 단추의 수직 스택에 동일한 높이를 사용합니다. 시각적 일관성을 위해 가능한 한 동일한 단추 높이를 사용하십시오.
>




**Use the system-defined corner radius.** The system defines corner radius values that provide a consistent visual style across apps and reinforce the interactivity of buttons. In Apple Watch Series 4 and later, corner radius values differ depending on whether the button is in a scrolling or nonscrolling view.
> 시스템 정의 코너 반지름을 사용합니다. 시스템은 앱 전체에서 일관된 시각적 스타일을 제공하고 버튼의 상호 작용을 강화하는 코너 반지름 값을 정의합니다. Apple Watch 시리즈 4 이상에서는 버튼이 스크롤 보기인지 아니면 비스크롤 보기인지에 따라 코너 반지름 값이 달라집니다.
>




![https://developer.apple.com/design/human-interface-guidelines/components/menus-and-actions/buttons/images/buttons-pinned-watchos_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/menus-and-actions/buttons/images/buttons-pinned-watchos_2x.png)

In nonscrolling views, buttons use a 22-point corner radius.
> 스크롤하지 않는 뷰에서 버튼은 22포인트 모서리 반경을 사용합니다.
>




![https://developer.apple.com/design/human-interface-guidelines/components/menus-and-actions/buttons/images/buttons-scroll-view-watchos_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/menus-and-actions/buttons/images/buttons-scroll-view-watchos_2x.png)

In scrolling views, buttons use a 9-point corner radius.
> 스크롤 보기에서 버튼은 9점 코너 반지름을 사용합니다.
>



