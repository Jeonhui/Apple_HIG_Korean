# **[components-selection-and-input] sliders**

## A slider is a horizontal track with a control, called a thumb, that people can adjust between a minimum and maximum value.
> 슬라이더는 사람들이 최소값과 최대값 사이에서 조정할 수 있는 엄지라고 불리는 컨트롤이 있는 수평 트랙입니다.
>




![https://developer.apple.com/design/human-interface-guidelines/images/intro/components/slider-intro-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/components/slider-intro-dark_2x.png)

As a slider’s value changes, the portion of track between the minimum value and the thumb fills with color. A slider can optionally display left and right icons that illustrate the meaning of the minimum and maximum values.
> 슬라이더의 값이 변경되면 최소값과 엄지손가락 사이의 트랙 부분이 색으로 채워집니다. 슬라이더는 최소값과 최대값의 의미를 나타내는 왼쪽 및 오른쪽 아이콘을 선택적으로 표시할 수 있습니다.
>




# **Best practices**

**Customize a slider’s appearance if it adds value.** You can adjust a slider’s appearance — including track color, thumb image and tint color, and left and right icons — to blend with your app’s design and communicate intent. A slider that adjusts image size, for example, could show a small image icon on the left and a large image icon on the right.
> 트랙 색상, 엄지 이미지 및 틴트 색상, 좌우 아이콘을 포함하여 슬라이더의 모양을 조정하여 앱의 디자인과 혼합하고 의도를 전달할 수 있습니다. 예를 들어, 이미지 크기를 조정하는 슬라이더는 왼쪽에 작은 이미지 아이콘을 표시하고 오른쪽에 큰 이미지 아이콘을 표시할 수 있습니다.
>




**Use familiar slider directions.** People expect the minimum and maximum sides of sliders to be consistent in all apps, with minimum values on the leading side and maximum values on the trailing side (for horizontal sliders) and minimum values at the bottom and maximum values at the top (for vertical sliders). For example, people expect to be able to move a horizontal slider that represents a percentage from 0 percent on the leading side to 100 percent on the trailing side.
> 익숙한 슬라이더 방향을 사용하십시오. 사람들은 모든 앱에서 슬라이더의 최소 및 최대 측면이 일관적일 것으로 예상하며, 선행 측면과 후행 측면의 최대값은 (수평 슬라이더의 경우), 하단의 최소값과 상단의 최대값은 (수직 슬라이더의 경우) 일치합니다. 예를 들어, 사람들은 선행 쪽의 0%에서 후행 쪽의 100%로 백분율을 나타내는 수평 슬라이더를 이동할 수 있을 것으로 기대합니다.
>




**Consider supplementing a slider with a corresponding text field and stepper.** Especially when a slider represents a wide range of values, people may appreciate seeing the exact slider value and having the ability to enter a specific value in a text field. Adding a stepper provides a convenient way for people to increment in whole values. For related guidance, see [Text fields](../components/selection-and-input/text-fields) and [Steppers](../components/selection-and-input/steppers).
> 슬라이더를 해당 텍스트 필드와 스테퍼로 보완하는 것을 고려해 보십시오. 특히 슬라이더가 광범위한 값을 나타내는 경우 정확한 슬라이더 값을 보고 텍스트 필드에 특정 값을 입력할 수 있는 능력을 갖는 것이 좋습니다. 스테퍼를 추가하면 사람들이 전체 값을 쉽게 증가시킬 수 있습니다. 관련 지침은 텍스트 필드 및 스텝퍼를 참조하십시오.
>




![https://developer.apple.com/design/human-interface-guidelines/components/selection-and-input/sliders/images/sliders-text-field_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/selection-and-input/sliders/images/sliders-text-field_2x.png)

# **Platform considerations**

*Not supported in tvOS.*

# **iOS, iPadOS**

**Don’t use a slider to adjust audio volume.** If you need to provide volume control in your app, use a volume view, which is customizable and includes a volume-level slider and a control for changing the active audio output device. For guidance, see [Playing audio](../patterns/playing-audio).
> 슬라이더를 사용하여 오디오 볼륨을 조정하지 마십시오. 앱에서 볼륨 컨트롤을 제공해야 하는 경우 볼륨 보기를 사용자 지정할 수 있으며 볼륨 수준 슬라이더와 활성 오디오 출력 장치를 변경하는 컨트롤이 포함되어 있습니다. 자세한 내용은 오디오 재생을 참조하십시오.
>




# **macOS**

Sliders in macOS can also include tick marks, making it easier for people to pinpoint a specific value within the range.
> macOS의 슬라이더는 체크 표시를 포함할 수 있어 사람들이 범위 내의 특정 값을 더 쉽게 찾을 수 있다.
>




In a linear slider without tick marks, the thumb is round, and the portion of track between the minimum value and the thumb is filled with color. In a linear slider with tick marks, the thumb is directional — pointing toward the tick marks — and the track isn’t tinted. A linear slider often includes supplementary icons that illustrate the meaning of the minimum and maximum values.
> 체크 표시가 없는 선형 슬라이더에서 엄지손가락은 둥글고 최소값과 엄지손가락 사이의 트랙 부분은 색상으로 채워집니다. 눈금 표시가 있는 선형 슬라이더에서 엄지손가락이 눈금 표시 쪽을 가리키며 트랙은 색이 지정되지 않습니다. 선형 슬라이더에는 종종 최소값과 최대값의 의미를 나타내는 보조 아이콘이 포함됩니다.
>




In a circular slider, the thumb appears as a small circle. Tick marks, when enabled, appear as evenly spaced dots around the circumference of the slider.
> 원형 슬라이더에서 엄지손가락은 작은 원으로 나타납니다. 눈금 표시가 활성화된 경우 슬라이더 둘레에 균일한 간격의 점으로 표시됩니다.
>




![https://developer.apple.com/design/human-interface-guidelines/components/selection-and-input/sliders/images/sliders-no-tick-marks_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/selection-and-input/sliders/images/sliders-no-tick-marks_2x.png)

Linear slider without tick marks

![https://developer.apple.com/design/human-interface-guidelines/components/selection-and-input/sliders/images/sliders-tick-marks_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/selection-and-input/sliders/images/sliders-tick-marks_2x.png)

Linear slider with tick marks

![https://developer.apple.com/design/human-interface-guidelines/components/selection-and-input/sliders/images/sliders-circular_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/selection-and-input/sliders/images/sliders-circular_2x.png)

Circular slider

**Consider giving live feedback as the value of a slider changes.** Live feedback shows people results in real time. For example, your Dock icons are dynamically scaled when adjusting the Size slider in Dock settings.
> 슬라이더의 값이 변경될 때 실시간 피드백을 제공하는 것을 고려해 보십시오. 실시간 피드백은 사람들에게 실시간으로 결과를 보여줍니다. 예를 들어, 도킹 설정에서 크기 슬라이더를 조정할 때 도킹 아이콘의 크기가 동적으로 조정됩니다.
>




**Choose a slider style that matches peoples’ expectations.** A horizontal slider is ideal when moving between a fixed starting and ending point. For example, a graphics app might offer a horizontal slider for setting the opacity level of an object between 0 and 100 percent. Use circular sliders when values repeat or continue indefinitely. For example, a graphics app might use a circular slider to adjust the rotation of an object between 0 and 360 degrees. An animation app might use a circular slider to adjust how many times an object spins when animated — four complete rotations equals four spins, or 1440 degrees of rotation.
> 사람들의 기대에 맞는 슬라이더 스타일을 선택하세요. 고정된 시작점과 종료점 사이를 이동할 때는 수평 슬라이더가 이상적입니다. 예를 들어 그래픽 앱은 개체의 불투명도 수준을 0에서 100% 사이로 설정하기 위한 수평 슬라이더를 제공할 수 있습니다. 값이 무한정 반복되거나 계속될 때 원형 슬라이더를 사용합니다. 예를 들어 그래픽 앱은 원형 슬라이더를 사용하여 물체의 회전을 0도에서 360도 사이로 조정할 수 있습니다. 애니메이션 앱은 원형 슬라이더를 사용하여 애니메이션 시 물체가 회전하는 횟수를 조정할 수 있습니다. 4번의 완전 회전은 4번의 회전 또는 1440도의 회전과 같습니다.
>




**Consider using a label to introduce a slider.** Labels generally use [sentence-style capitalization](https://help.apple.com/applestyleguide/#/apsgb744e4a3?sub=apdca93e113f1d64) and end with a colon. For guidance, see [Labels](../components/layout-and-organization/labels).
> 레이블을 사용하여 슬라이더를 도입하는 것을 고려해 보십시오. 레이블은 일반적으로 문장 스타일의 대문자를 사용하고 콜론으로 끝납니다. 자세한 내용은 레이블을 참조하십시오.
>




**Use tick marks to increase clarity and accuracy.** Tick marks help people understand the scale of measurements and make it easier to locate specific values.
> 눈금 표시를 사용하여 선명도와 정확도를 높입니다. 눈금 표시는 사람들이 측정값의 크기를 이해하고 특정 값을 더 쉽게 찾을 수 있도록 도와줍니다.
>




![https://developer.apple.com/design/human-interface-guidelines/components/selection-and-input/sliders/images/sliders-labels_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/selection-and-input/sliders/images/sliders-labels_2x.png)

**Consider adding labels to tick marks for even greater clarity.** Labels can be numbers or words, depending on the slider's values. It’s unnecessary to label every tick mark unless doing so is needed to reduce confusion. In many cases, labeling only the minimum and maximum values is sufficient. When the values of the slider are nonlinear, like in the Energy Saver settings pane, periodic labels provide context. It's also a good idea to provide a [help tag](../patterns/offering-help) that displays the value of the thumb when people hold their pointer over it.
> 슬라이더의 값에 따라 레이블을 숫자 또는 단어로 표시할 수 있습니다. 혼란을 줄이기 위해 그렇게 할 필요가 없는 한 모든 체크 표시에 라벨을 붙일 필요가 없다. 대부분의 경우 최소값과 최대값에만 레이블을 지정하면 충분합니다. 에너지 절약 설정 창에서와 같이 슬라이더 값이 비선형적인 경우 주기적 레이블이 컨텍스트를 제공합니다. 또한 사람들이 포인터를 엄지 위에 놓으면 엄지 손가락의 값이 표시되는 도움말 태그를 제공하는 것도 좋은 방법입니다.
>




# **watchOS**

A slider is a horizontal track — appearing as a set of discrete steps or as a continuous bar — that represents a finite range of values. People can tap buttons on the sides of the slider to increase or decrease its value by a predefined amount.
> 슬라이더는 한정된 범위의 값을 나타내는 수평 트랙(개별 단계 집합 또는 연속 막대로 표시)입니다. 슬라이더의 측면에 있는 버튼을 눌러 슬라이더의 값을 미리 정의된 양만큼 늘리거나 줄일 수 있습니다.
>




![https://developer.apple.com/design/human-interface-guidelines/components/selection-and-input/sliders/images/sliders-watchos_2x.png](https://developer.apple.com/design/human-interface-guidelines/components/selection-and-input/sliders/images/sliders-watchos_2x.png)

