---
title: UTBLDialogWidget
type: class
aliases: UTBLDialogWidget
share: false

---

# UTBLDialogWidget





Inherits from [UTBLScreenWidget](/docs/SDK/Source/Classes/classUTBLScreenWidget.md), [UTBLUserWidget](/docs/SDK/Source/Classes/classUTBLUserWidget.md), UUserWidget

## Public Functions

|                | Name           |
| -------------- | -------------- |
| void | **[[ChangeText]]**(const FText & Title, const FText & Body) |
| [FDialogHandle](/docs/SDK/Source/Classes/structFDialogHandle.md) | **[[GetDialogHandle]]**() const |
| void | **[[ProcessButtonClick]]**(EDialogButtons ButtonClicked) |
| | **[[UTBLDialogWidget]]**() |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| [FDialogHandle](/docs/SDK/Source/Classes/structFDialogHandle.md) | **[[DialogHandle]]**  |
| EDialogTypes | **[[DialogType]]**  |
| ULocalPlayer * | **[[m_pLocalOwningPlayer]]**  |

-------------------------------

Updated on 2023-07-04 at 02:31:00 +0200