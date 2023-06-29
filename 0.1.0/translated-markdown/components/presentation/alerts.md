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

**Create succinct, logical button titles.** Aim for a one- or two-word title that describes the result of selecting the button. Prefer verbs and verb phrases that relate directly to the alert text — for example, “View All,” “Reply,” or “Ignore.” In informational alerts only, you can use “OK” for acceptance, avoiding “Yes” and “No.” Always use “Cancel” to title a button that cancels the alert’s action. As with all button titles, use [title-style capitalization](https://help.apple.com/applestyleguide/#/apsgb744e4a3?sub=apdca93e113f1d64) and no ending punctuation.
> 간결하고 논리적인 단추 제목을 만듭니다. 단추를 선택한 결과를 설명하는 한 두 단어 제목을 목표로 합니다. 경고 텍스트와 직접 관련된 동사 및 동사 구(예: "모두 보기", "응답" 또는 "무시")를 선호합니다. 정보 알림에서만 "확인"을 사용하여 "예"와 "아니오"를 피하도록 허용할 수 있습니다. 경고 작업을 취소하는 단추의 제목을 지정하려면 항상 "취소"를 사용하십시오. 모든 단추 제목과 마찬가지로 제목 스타일의 대문자를 사용하고 끝 문장 부호를 사용하지 마십시오.
>




**Avoid using OK as the default button title unless the alert is purely informational.** The meaning of “OK” can be unclear even in alerts that ask people to confirm that they want to do something. For example, does “OK” mean “OK, I want to complete the action” or “OK, I now understand the negative results my action would have caused”? A specific button title like “Erase,” “Convert,” “Clear,” or “Delete” helps people understand the action they’re taking.
> 경고가 순전히 정보를 제공하는 경우가 아니면 확인을 기본 단추 제목으로 사용하지 마십시오. "확인"의 의미는 사람들에게 무언가를 하고 싶은지 묻는 경고에서도 불분명할 수 있습니다. 예를 들어, "OK"는 "OK, 작업을 완료하고 싶다" 또는 "OK, 이제 내 작업이 초래했을 부정적인 결과를 이해한다"를 의미합니까? "지우기", "변환", "지우기" 또는 "삭제"와 같은 특정 단추 제목은 사용자가 수행하는 작업을 이해하는 데 도움이 됩니다.
>




**Place buttons where people expect.** In general, place the button people are most likely to choose on the trailing side in a row of buttons or at the top in a stack of buttons. Always place the default button on the trailing side of a row or at the top of a stack. Cancel buttons are typically on the leading side of a row or at the bottom of a stack.
> 사람들이 예상하는 곳에 버튼을 놓습니다. 일반적으로, 사람들이 선택할 가능성이 가장 높은 버튼을 버튼의 열에 놓거나 버튼의 맨 위에 배치합니다. 기본 버튼은 항상 행의 뒤쪽 또는 스택의 맨 위에 배치하십시오. 취소 단추는 일반적으로 행의 맨 앞이나 스택의 맨 아래에 있습니다.
>




**Identify destructive buttons.** If an alert button results in a destructive action, like deleting content, specify the destructive button style to help people recognize it.
> 삭제 단추를 식별합니다. 경고 단추로 인해 내용 삭제와 같은 삭제 작업이 발생할 경우 사용자가 쉽게 인식할 수 있도록 삭제 단추 스타일을 지정하십시오.
>




**Include a Cancel button when there’s a destructive action.** A Cancel button provides a clear, safe way to avoid a destructive action. Consider making the Cancel button the default button so that people must intentionally choose a button other than the default to continue with the destructive action. Always use the title “Cancel” for a button that cancels an alert’s action.
> 파괴 작업이 있을 때 취소 단추를 포함합니다. 취소 단추는 파괴 작업을 방지하는 명확하고 안전한 방법을 제공합니다. 삭제 작업을 계속하려면 사용자가 의도적으로 기본값이 아닌 다른 단추를 선택해야 하므로 취소 단추를 기본 단추로 설정하는 것을 고려하십시오. 알림 작업을 취소하는 단추에는 항상 "취소"라는 제목을 사용하십시오.
>




**Enable alternative ways to cancel an alert when it makes sense.** In addition to choosing a Cancel button, people appreciate using keyboard shortcuts or other quick ways to cancel an onscreen alert. For example:
> 다른 방법으로 알림을 취소할 수 있습니다. 취소 단추를 선택하는 것 외에도 키보드 단축키나 다른 빠른 방법으로 알림을 취소할 수 있습니다. 예:
>




| Action | Platform |  |
| --- | --- | --- |
| Exit to the Home Screen | iOS, iPadOS |  |
| Pressing Escape (Esc) or Command-Period (.) on an attached keyboard | macOS, iOS, iPadOS |  |
| Pressing Menu on the remote | tvOS |  |

# **Platform considerations**

*No additional considerations for tvOS or watchOS.*
> TVOS 또는 시계에 대한 추가 고려 사항 없음운영 체제
>




# **iOS, iPadOS**

**Use an action sheet — not an alert — to offer choices related to an intentional action.** For example, when people cancel the Mail message they’re editing, an action sheet provides three choices: delete the edits (or the entire draft), save the draft, or return to editing. Although an alert can also help people confirm or cancel an action that has destructive consequences, it doesn’t provide additional choices related to the action. For guidance, see [Action sheets](../components/presentation/action-sheets).
> 사용자가 편집 중인 메일 메시지를 취소할 때 작업 시트는 편집 내용 삭제(또는 전체 초안 저장) 또는 편집으로 돌아가기의 세 가지 선택사항을 제공합니다. 경고는 또한 사람들이 파괴적인 결과를 초래하는 작업을 확인하거나 취소하는 데 도움이 될 수 있지만, 해당 작업과 관련된 추가 선택을 제공하지는 않습니다. 자세한 내용은 작업 시트를 참조하십시오.
>




**When possible, avoid displaying an alert that scrolls.** Although an alert might scroll if the text size is large enough, be sure to minimize the potential for scrolling by keeping alert titles short and including a brief message only when necessary.
> 텍스트 크기가 충분히 크면 경보가 스크롤될 수 있지만 필요한 경우에만 경고 제목을 짧게 유지하고 간단한 메시지를 포함하여 스크롤 가능성을 최소화해야 합니다.
>




# **macOS**

**Use a caution symbol sparingly.** Using a caution symbol like `exclamationmark.triangle` too frequently in your alerts diminishes its significance. Use the symbol only when extra attention is really needed, as when confirming an action that might result in unexpected loss of data. Don’t use the symbol for tasks whose only purpose is to overwrite or remove data, such as a save or empty trash.
> 경고에 느낌표.삼각형과 같은 주의 기호를 너무 자주 사용하면 경고의 중요성이 감소합니다. 예기치 않은 데이터 손실을 초래할 수 있는 작업을 확인할 때와 같이, 추가적인 주의가 필요한 경우에만 기호를 사용하십시오. 저장 또는 휴지통 비우기와 같이 데이터를 덮어쓰거나 제거하는 것이 유일한 목적인 태스크에는 기호를 사용하지 마십시오.
>



