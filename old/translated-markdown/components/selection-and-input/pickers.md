# **[components-selection-and-input] pickers**

## A picker displays one or more scrollable lists of distinct values that people can choose from.
> 선택 도구는 사용자가 선택할 수 있는 하나 이상의 스크롤 가능한 고유 값 목록을 표시합니다.
>




![https://developer.apple.com/design/human-interface-guidelines/images/intro/components/pickers-intro-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/components/pickers-intro-dark_2x.png)

The system provides several styles of pickers, each of which offers different types of selectable values and has a different appearance. The exact values shown in a picker, and their order, depend on the device language.
> 이 시스템은 여러 스타일의 피커를 제공하며, 각 피커는 서로 다른 유형의 선택 가능한 값을 제공하고 모양이 다릅니다. 선택 도구에 표시되는 정확한 값과 순서는 장치 언어에 따라 다릅니다.
>




Pickers help people enter information by letting them choose single or multipart values. Date pickers specifically offer additional ways to choose values, like selecting a day in a calendar view or entering dates and times using a numeric keypad.
> 피커는 사람들이 단일 또는 다중 부분 값을 선택하도록 함으로써 정보를 입력하는 것을 돕는다. 달력 보기에서 날짜를 선택하거나 숫자 키패드를 사용하여 날짜와 시간을 입력하는 것과 같은 값을 선택할 수 있는 추가적으로 제공합니다.
>




# **Best practices**

**Consider using a picker to offer medium-to-long lists of items.** If you need to display a fairly short list of choices, consider using a [pull-down button](../components/menus-and-actions/pull-down-buttons) instead of a picker. Although a picker makes it easy to scroll quickly through many items, it may add too much visual weight to a short list of items. On the other hand, if you need to present a very large set of items, consider using a [list or table](../components/layout-and-organization/lists-and-tables). Lists and tables can adjust in height, and tables can include an index, which makes it much faster to target a section of the list.
> 중간에서 긴 항목 목록을 제공하려면 선택 도구를 사용하는 것이 좋습니다. 선택 항목 목록을 짧게 표시하려면 선택 도구 대신 풀다운 단추를 사용하는 것이 좋습니다. 선택 도구를 사용하면 많은 항목을 빠르게 스크롤할 수 있지만 짧은 항목 목록에 너무 많은 시각적 가중치가 추가될 수 있습니다. 반면, 매우 큰 항목 집합을 표시해야 하는 경우 목록이나 표를 사용하는 것을 고려해 보십시오. 목록과 테이블은 높이를 조정할 수 있으며, 테이블은 인덱스를 포함할 수 있으므로 목록의 한 섹션을 훨씬 빨리 대상으로 지정할 수 있습니다.
>




**Use predictable and logically ordered values.** Many values in a picker may be hidden before people interact with it. It’s best when people can predict what the hidden values are, such as with an alphabetized list of countries, so they can move through the items quickly.
> 예측 가능하고 논리적으로 정렬된 값을 사용하십시오. 사람들이 선택기와 상호 작용하기 전에 선택기의 많은 값이 숨겨질 수 있습니다. 사람들이 국가 목록을 알파벳 순으로 나열한 것처럼 숨겨진 가치가 무엇인지 예측할 수 있을 때가 가장 좋습니다. 그래서 그들은 항목을 빠르게 이동할 수 있습니다.
>




**Avoid switching screens to show a picker.** A picker works well when displayed in context, below or in proximity to the field being edited. A picker typically appears at the bottom of the screen or in a popover.
> 화면을 전환하여 선택기를 표시하지 마십시오. 편집 중인 필드 아래 또는 근처에 상황에 따라 선택기가 표시될 때 잘 작동합니다. 선택 도구는 일반적으로 화면 하단이나 팝업창에 나타납니다.
>




**Consider providing less granularity when specifying minutes in a date picker.** By default, a minute list includes 60 values (0 to 59). You can optionally increase the minute interval as long as it divides evenly into 60. For example, you might want quarter-hour intervals (0, 15, 30, and 45).
> 달력 보기에서 분을 지정할 때 세분성을 줄이는 것이 좋습니다. 기본적으로 분 목록에는 60개의 값(0 ~ 59)이 포함됩니다. 선택적으로 분 간격을 60으로 균등하게 나누는 한 늘릴 수 있습니다. 예를 들어, 25시간 간격(0, 15, 30 및 45)을 원할 수 있습니다.
>




# **Platform considerations**

# **iOS, iPadOS**

A date picker is an efficient interface for selecting a specific date, time, or both, using touch, a keyboard, or a pointing device. You can display a date picker in one of the following styles:
> 달력 보기는 터치, 키보드 또는 포인팅 장치를 사용하여 특정 날짜, 시간 또는 둘 모두를 선택할 수 있는 효율적인 인터페이스입니다. 다음 유형 중 하나로 달력 보기를 표시할 수 있습니다.
>




- Compact — A button that displays editable date and time content in a modal view.
- >  압축 - 편집 가능한 날짜 및 시간 내용을 모달 보기로 표시하는 단추입니다.

- Inline — For time only, a button that displays wheels of values; for dates and times, an inline calendar view.
- >  인라인 - 시간에 한해 값의 휠을 표시하는 단추이며, 날짜 및 시간에 대해서는 인라인 일정관리 보기를 표시합니다.

- Wheels — A set of scrolling wheels that also supports data entry through built-in or external keyboards.
- >  휠 — 내장 키보드 또는 외부 키보드를 통한 데이터 입력도 지원하는 스크롤 휠 세트입니다.

- Automatic — A system-determined style based on the current platform and date picker mode.
- >  자동 - 현재 플랫폼 및 달력 보기 모드에 따라 시스템에서 결정되는 스타일입니다.


A date picker has four modes, each of which presents a different set of selectable values.
> 달력 보기에는 네 가지 모드가 있으며, 각 모드는 서로 다른 선택 가능한 값 집합을 나타냅니다.
>




- Date — Displays months, days of the month, and years.
- >  날짜 — 월, 일 및 연도를 표시합니다.

- Time — Displays hours, minutes, and (optionally) an AM/PM designation.
- >  시간 — 시간, 분 및 (선택적으로) AM/PM 지정을 표시합니다.

- Date and time — Displays dates, hours, minutes, and (optionally) an AM/PM designation.
- >  날짜 및 시간 — 날짜, 시간, 분 및 (선택적으로) AM/PM 지정을 표시합니다.

- Countdown timer — Displays hours and minutes, up to a maximum of 23 hours and 59 minutes. This mode isn’t available in the inline or compact styles.
- >  카운트다운 타이머 — 시간과 분을 최대 23시간 59분까지 표시합니다. 이 모드는 인라인 또는 컴팩트 스타일에서 사용할 수 없습니다.


The exact values shown in a date picker, and their order, depend on the device location.
> 달력 보기에 표시되는 정확한 값과 순서는 장치 위치에 따라 다릅니다.
>




Here are several examples of date pickers showing different combinations of style and mode.
> 다음은 스타일과 모드의 다양한 조합을 보여주는 데이트 선택기의 몇 가지 예입니다.
>




• [Compact](../components/selection-and-input/pickers#)
• [Inline](../components/selection-and-input/pickers#)
• [Wheels](../components/selection-and-input/pickers#)

-

![https://developer.apple.com/design/human-interface-guidelines/components/selection-and-input/pickers/images/picker-compact-closed_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/selection-and-input/pickers/images/picker-compact-closed_2x.png)

Scheduled summary settings uses a compact date picker in time mode.
> 예약된 요약 설정은 시간 모드에서 소형 달력 보기를 사용합니다.
>




![https://developer.apple.com/design/human-interface-guidelines/components/selection-and-input/pickers/images/picker-compact-open_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/selection-and-input/pickers/images/picker-compact-open_2x.png)

When people tap the date picker, it reveals time values within a modal view.
> 사람들이 달력 보기를 누르면 모달 보기 내에 시간 값이 표시됩니다.
>





**Use a compact date picker when space is constrained.** The compact style displays a button that shows the current value in your app’s accent color. When people tap the button, the date picker opens a modal view, providing access to a familiar calendar-style editor and time picker. Within the modal view, people can make multiple edits to dates and times before tapping outside the view to confirm their choices.
> 공간이 제한된 경우 콤팩트 달력 보기를 사용하십시오. 콤팩트 스타일은 앱의 액센트 색상으로 현재 값을 표시하는 단추를 표시합니다. 사람들이 단추를 누르면 달력 보기가 열리고 익숙한 달력 스타일의 편집기와 시간 보기에 액세스할 수 있습니다. 모달 보기 내에서 사용자는 보기 외부를 눌러 선택 사항을 확인하기 전에 날짜와 시간을 여러 번 편집할 수 있습니다.
>




# **macOS**

**Choose a date picker style that suits your app.** There are two styles of date pickers in macOS: textual and graphical. The textual style is useful when you’re working with limited space and you expect people to make specific date and time selections. The graphical style is useful when you want to give people the option of browsing through days in a calendar or selecting a range of dates, or when the look of a clock face is appropriate for your app.
> 당신의 앱에 맞는 달력 보기 스타일을 선택하세요. macOS에는 텍스트와 그래픽의 두 가지 스타일의 달력 보기가 있습니다. 텍스트 스타일은 제한된 공간에서 작업할 때 사용자가 특정 날짜 및 시간을 선택해야 할 때 유용합니다. 그래픽 스타일은 사람들에게 달력에서 며칠 동안 검색하거나 날짜 범위를 선택할 수 있는 옵션을 제공하거나 앱에 시계 모양이 적합할 때 유용합니다.
>




For developer guidance, see [NSDatePicker](https://developer.apple.com/documentation/appkit/nsdatepicker).

# **tvOS**

Pickers are available in tvOS with SwiftUI. For developer guidance, see [Picker](https://developer.apple.com/documentation/swiftui/picker).
> 피커는 스위프트와 함께 TVOS에서 사용할 수 있습니다.UI. 개발자 지침은 선택기를 참조하십시오.
>




# **watchOS**

Pickers display lists of items that people navigate using the Digital Crown, which enables a precise and engaging way to manage selections.
> 피커는 사람들이 디지털 크라운을 사용하여 탐색하는 항목의 목록을 표시하므로 선택 항목을 정확하고 매력적으로 관리할 수 있습니다.
>




Pickers present their items in the following styles.
> 피커는 다음 스타일로 아이템을 제시합니다.
>




![https://developer.apple.com/design/human-interface-guidelines/components/selection-and-input/pickers/images/pickers-list_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/selection-and-input/pickers/images/pickers-list_2x.png)

**List picker.** Displays text and images in a scrolling list. In addition to the selected item, a list picker shows the previous and next items when they're available.
> 목록 선택기. 스크롤 목록에 텍스트와 이미지를 표시합니다. 목록 선택기는 선택한 항목 외에도 이전 항목과 다음 항목을 사용할 수 있을 때 표시합니다.
>




![https://developer.apple.com/design/human-interface-guidelines/components/selection-and-input/pickers/images/pickers-stack_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/selection-and-input/pickers/images/pickers-stack_2x.png)

**Stack picker.**Displays images in a card stack interface. As people scroll, images animate into position with the selected image on top.
> 스택 선택기.카드 스택 인터페이스에 이미지를 표시합니다. 사용자가 스크롤할 때 이미지는 선택한 이미지를 맨 위에 두고 제 위치로 애니메이션됩니다.
>




![https://developer.apple.com/design/human-interface-guidelines/components/selection-and-input/pickers/images/pickers-sequence_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/selection-and-input/pickers/images/pickers-sequence_2x.png)

**Sequence picker.**Displays one image from a sequence of images. As people turn the Digital Crown, the picker displays the previous or next image in the sequence without animations.
> 시퀀스 선택기.일련의 이미지 중 하나의 이미지를 표시합니다. 사람들이 디지털 크라운을 돌리면 선택기는 애니메이션 없이 이전 또는 다음 이미지를 순서대로 표시합니다.
>




You can configure a picker to display an outline, caption, and scrolling indicator. These elements help identify the picker onscreen and help people navigate its contents.
> 윤곽선, 캡션 및 스크롤 표시기를 표시하도록 선택기를 구성할 수 있습니다. 이러한 요소는 화면에서 선택기를 식별하고 사용자가 내용을 탐색하는 데 도움이 됩니다.
>




**Use captions to clarify the meaning of items or of the picker itself.** You can assign unique captions to an item if it helps to clarify its meaning. Alternatively, you can assign the same caption to all items to clarify the purpose of the picker itself.
> 캡션을 사용하여 항목 또는 선택 도구 자체의 의미를 명확히 합니다. 항목의 의미를 명확히 하는 데 도움이 되는 경우 항목에 고유한 캡션을 할당할 수 있습니다. 또는 모든 항목에 동일한 캡션을 할당하여 선택 도구 자체의 목적을 명확히 할 수 있습니다.
>




**Display a scroll indicator when the total number of items might not be obvious.** A scroll indicator reflects the total number of items in a picker and indicates the current position within the list. A scroll indicator is unnecessary when the sequence and number of items is obvious, such as when specifying the number of seconds for a timer.
> 총 항목 수가 명확하지 않을 때 스크롤 표시기를 표시합니다. 스크롤 표시기는 선택기의 총 항목 수를 나타내며 목록 내의 현재 위치를 나타냅니다. 타이머에 초를 지정하는 경우와 같이 순서와 항목 수가 명확한 경우에는 스크롤 표시기가 필요하지 않습니다.
>




![https://developer.apple.com/design/human-interface-guidelines/components/selection-and-input/pickers/images/pickers-scroller_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/selection-and-input/pickers/images/pickers-scroller_2x.png)
