---
title: UChatWidget
type: class
aliases: UChatWidget
share: false

---

# UChatWidget





Inherits from UWidget

## Public Functions

|                | Name           |
| -------------- | -------------- |
| void | **[[SetAlwaysVisible]]**(bool InAlwaysVisible) |
| | **[[UChatWidget]]**() |
| void | **[[UsedChat]]**() |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| FAddedChatLineSignature | **[[OnAddedChatLine]]**  |
| FChangeAlwaysVisible | **[[OnChangedAlwaysVisible]]**  |
| FEnterInputModeSignature | **[[OnEnterInputMode]]**  |
| FEnterLastChannelInputModeSignature | **[[OnEnterLastChannelInputMode]]**  |
| FOnGenerateRowChatLine | **[[OnGenerateRowEvent]]**  |
| int32 | **[[SecondsToConsiderMessageFresh]]**  |
| bool | **[[bAlwaysVisible]]**  |
| bool | **[[bShowTimestamps]]**  |
| bool | **[[bUseAbbreviatedChatHistory]]**  |
| UWidget::FGetBool | **[[bUseAbbreviatedChatHistoryDelegate]]**  |

-------------------------------

Updated on 2023-07-04 at 02:30:59 +0200