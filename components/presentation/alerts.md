# **[components-presentation] alerts**

## An alert gives people critical information they need right away.
> 경보는 사람들에게 그들이 필요로 하는 중요한 정보를 즉시 제공한다.
>




![https://developer.apple.com/design/human-interface-guidelines/images/intro/components/alert-intro-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/components/alert-intro-dark_2x.png)

For example, an alert can tell people about a problem, warn them when their action might destroy data, and give them an opportunity to confirm a purchase or another important action they initiated.
> 예를 들어 경고는 사용자에게 문제를 알리고, 작업이 데이터를 파괴할 수 있는 시기를 경고하며, 사용자가 시작한 구매 또는 기타 중요한 작업을 확인할 수 있는 기회를 제공할 수 있습니다.
>




# **Best practices**

**Use alerts sparingly.** Alerts give people important information, but they interrupt the current task to do so. Encourage people to pay attention to your alerts by making certain that each one offers only essential information and useful actions.
> 경고는 사용자에게 중요한 정보를 제공하지만 이를 위해 현재 작업을 중단합니다. 각 경고가 중요한 정보와 유용한 작업만 제공하는지 확인하여 사용자의 경고에 주의를 기울이도록 권장합니다.
>




**Avoid using an alert merely to provide information.** People don’t appreciate an interruption from an alert that’s informative, but not actionable. If you need to provide only information, prefer finding an alternative way to communicate it within the relevant context. For example, when a server connection is unavailable, Mail displays an indicator that people can choose to learn more.
> 정보를 제공하기 위해서만 경고를 사용하지 마십시오. 사람들은 유용하지만 실행 가능하지 않은 경고로 인한 중단을 인식하지 못합니다. 정보만 제공해야 하는 경우 관련 컨텍스트 내에서 정보를 전달할 수 있는 다른 방법을 찾는 것을 선호합니다. 예를 들어, 서버 연결을 사용할 수 없는 경우, 메일은 사용자가 추가 학습을 선택할 수 있는 표시기를 표시합니다.
>




**Avoid displaying alerts for common, undoable actions, even when they’re destructive.** For example, you don’t need to alert people about data loss every time they delete an email or file because they do so with the intention of discarding data, and they can undo the action. In comparison, when people take an uncommon destructive action that they can’t undo, it's important to display an alert in case they initiated the action accidentally.
> 예를 들어 전자 메일이나 파일을 삭제할 때마다 사용자에게 데이터 손실을 경고할 필요가 없으며, 사용자가 작업을 취소할 수 있기 때문에 전자 메일 또는 파일을 삭제할 때마다 데이터 손실에 대해 경고할 필요가 없습니다. 이에 비해, 사람들이 되돌릴 수 없는 비정상적인 파괴적인 행동을 취할 때, 그들이 실수로 행동을 시작했을 때를 대비하여 경고를 표시하는 것이 중요하다.
>




**Avoid showing an alert when your app starts.** If you need to inform people about new or important information the moment they open your app, design a way to make the information easily discoverable. If your app detects a problem at startup, like no network connection, consider alternative ways to let people know. For example, you could show cached or placeholder data and a nonintrusive label that describes the problem.
> 앱이 시작될 때 경고를 표시하지 않도록 합니다. 앱을 여는 순간 사람들에게 새로운 정보나 중요한 정보를 알려야 할 경우 정보를 쉽게 검색할 수 있는 방법을 설계하십시오. 시작 시 네트워크 연결이 없는 등의 문제가 감지되면 다른 방법으로 사람들에게 알릴 수 있습니다. 예를 들어 캐시 또는 자리 표시자 데이터와 문제를 설명하는 비침입 레이블을 표시할 수 있습니다.
>




# **Anatomy**

An alert is a modal view that can look different in different platforms and devices.
> 알림은 플랫폼과 장치에 따라 다르게 보일 수 있는 모달 뷰입니다.
>




• [iOS](../components/presentation/alerts#)
• [macOS](../components/presentation/alerts#)
• [watchOS](../components/presentation/alerts#)

-

![https://developer.apple.com/design/human-interface-guidelines/patterns/accessing-private-data/images/permission-request-3_2x.png](https://developer.apple.com/design/human-interface-guidelines/patterns/accessing-private-data/images/permission-request-3_2x.png)


# **Content**

In all platforms, alerts display a title, optional informative text, and up to three buttons. On some platforms, alerts can include additional elements.
> 모든 플랫폼에서 알림은 제목, 선택적 정보 텍스트 및 최대 세 개의 단추를 표시합니다. 일부 플랫폼에서는 알림에 추가 요소가 포함될 수 있습니다.
>




| Element | iOS, iPadOS | macOS | tvOS | watchOS | Guidance |
| --- | --- | --- | --- | --- | --- |
| Title | ● | ● | ● | ● | Write a brief sentence or phrase that describes the situation. |
| Informative text | ● | ● | ● | ● | Write a short message if you need to describe the consequences of the situation, suggest solutions or alternatives, or remind people when they can't undo an action. |
| Buttons | ● | ● | ● | ● | Prefer a two-button alert to give people a clear choice; provide an additional button if necessary. The default button can cancel the alert or perform the most likely nondestructive action. See buttons. |
| Icon |  | ● |  |  | macOS automatically displays your app icon in the alert, but you can supply an alternative icon or symbol. See macos. |
| Suppression checkbox |  | ● |  |  | You can configure repeating alerts to let people suppress subsequent occurrences of the same alert. |
| Accessory view |  | ● |  |  | You can append a custom view if it's necessary to provide additional information. |
| Help button |  | ● |  |  | You can include a Help button that opens your help documentation. See help buttons. |
| Text field | ● | ● |  |  | Include a text field only if you need people's input to resolve the situation. |

**In all alert copy, be direct, and use a neutral, approachable tone.** Alerts often describe problems and serious situations, so avoid being oblique or accusatory, or masking the severity of the issue.
> 모든 경고 복사본에서는 직접적으로 사용하고 중립적이고 접근 가능한 어조를 사용하십시오. 경고는 종종 문제와 심각한 상황을 설명하므로, 비스듬히 또는 비난하거나 문제의 심각성을 숨기지 않도록 합니다.
>




**Write a title that clearly and succinctly describes the situation.** You need to help people quickly understand the situation, so be complete and specific, without being verbose. As much as possible, describe what happened, the context in which it happened, and why. Avoid writing a title that doesn’t convey useful information — like “Error” or “Error 329347 occurred” — but also avoid overly long titles that wrap to more than two lines. If the title is a complete sentence, use [sentence-style capitalization](https://help.apple.com/applestyleguide/#/apsgb744e4a3?sub=apdca93e113f1d64) and appropriate ending punctuation. If the title is a sentence fragment, use title-style capitalization, and don’t add ending punctuation.
> 상황을 명확하고 간결하게 묘사하는 제목을 써라. 사람들이 상황을 빨리 이해할 수 있도록 도와줄 필요가 있기 때문에 장황하게 말하지 말고 완전하고 구체적이어야 한다. 가능한 한, 무슨 일이 일어났는지, 그 일이 일어난 맥락과 그 이유를 설명하십시오. "오류" 또는 "오류 329347 발생"과 같이 유용한 정보를 전달하지 않는 제목은 쓰지 않도록 하되, 두 줄 이상으로 묶는 지나치게 긴 제목은 쓰지 않도록 합니다. 제목이 완전한 문장인 경우, 문장 스타일의 대문자와 적절한 끝 문장 부호를 사용하십시오. 제목이 문장 조각인 경우 제목 스타일의 대문자를 사용하고 끝 문장 부호를 추가하지 마십시오.
>




**Include informative text only if it adds value.** If you need to add an informative message, keep it as short as possible, using complete sentences, sentence-style capitalization, and appropriate punctuation.
> 유익한 텍스트는 가치를 추가하는 경우에만 포함하십시오. 유익한 메시지를 추가해야 할 경우에는 완전한 문장, 문장 스타일의 대문자 및 적절한 구두점을 사용하여 가능한 한 짧게 유지하십시오.
>




**Avoid explaining alert buttons.** If your alert text and button titles are clear, you don't need to explain what the buttons do. In rare cases where you need to provide guidance on choosing a button, use a term like *choose* to account for people's current device and interaction method, and refer to a button using its exact title without quotes.
> 경고 단추에 대해 설명하지 마십시오. 경고 텍스트와 단추 제목이 명확하면 단추의 기능을 설명할 필요가 없습니다. 단추 선택에 대한 지침을 제공해야 하는 드문 경우에는 사용자의 현재 장치 및 상호 작용 방법을 설명하기 위해 선택과 같은 용어를 사용하고 따옴표 없이 정확한 제목을 사용하여 단추를 참조하십시오.
>




# **Buttons**

