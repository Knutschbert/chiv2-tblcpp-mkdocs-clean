---
title: UTBLDialogManager
type: class
aliases: UTBLDialogManager
share: false

---

# UTBLDialogManager





Inherits from [UTBLScreenManager](/docs/SDK/Source/Classes/classUTBLScreenManager.md), [UTBLUserWidget](/docs/SDK/Source/Classes/classUTBLUserWidget.md), [ITBLKeymapWidgetInterface](/docs/SDK/Source/Classes/classITBLKeymapWidgetInterface.md), UUserWidget

## Public Functions

|                | Name           |
| -------------- | -------------- |
| [FDialogHandle](/docs/SDK/Source/Classes/structFDialogHandle.md) | **[[ChangeDialogText]]**(const [FDialogHandle](/docs/SDK/Source/Classes/structFDialogHandle.md) & DialogHandle, const FText & Title, const FText & Body) |
| [FDialogHandle](/docs/SDK/Source/Classes/structFDialogHandle.md) | **[[CloseDialog]]**(const [FDialogHandle](/docs/SDK/Source/Classes/structFDialogHandle.md) & DialogHandle) |
| bool | **[[IsDialogActive]]**([FDialogHandle](/docs/SDK/Source/Classes/structFDialogHandle.md) InDialogHandle) |
| [UTBLDialogWidget](/docs/SDK/Source/Classes/classUTBLDialogWidget.md) * | **[[OnCreateCancelWorkingDialog]]**(const FText & Title, const FText & Body) |
| [UTBLDialogWidget](/docs/SDK/Source/Classes/classUTBLDialogWidget.md) * | **[[OnCreateExitDialog]]**(const FText & Title, const FText & Body) |
| [UTBLDialogWidget](/docs/SDK/Source/Classes/classUTBLDialogWidget.md) * | **[[OnCreateNoButtonsDialog]]**(const FText & Title, const FText & Body) |
| [UTBLDialogWidget](/docs/SDK/Source/Classes/classUTBLDialogWidget.md) * | **[[OnCreateNoButtonsWorkingDialog]]**(const FText & Title, const FText & Body) |
| [UTBLDialogWidget](/docs/SDK/Source/Classes/classUTBLDialogWidget.md) * | **[[OnCreateOkCancelDialog]]**(const FText & Title, const FText & Body) |
| [UTBLDialogWidget](/docs/SDK/Source/Classes/classUTBLDialogWidget.md) * | **[[OnCreateOkDialog]]**(const FText & Title, const FText & Body) |
| [UTBLDialogWidget](/docs/SDK/Source/Classes/classUTBLDialogWidget.md) * | **[[OnCreateYesNoDialog]]**(const FText & Title, const FText & Body) |
| [FDialogHandle](/docs/SDK/Source/Classes/structFDialogHandle.md) | **[[ShowCancelWorkingDialog]]**(FText Title, FText Body, FDialogButtonDelegate CancelDelegate, int32 DialogPriority) |
| [FDialogHandle](/docs/SDK/Source/Classes/structFDialogHandle.md) | **[[ShowExitDialog]]**(FText Title, FText Body, FDialogButtonDelegate ExitDelegate, int32 DialogPriority) |
| [FDialogHandle](/docs/SDK/Source/Classes/structFDialogHandle.md) | **[[ShowNoButtonsDialog]]**(FText Title, FText Body, int32 DialogPriority) |
| [FDialogHandle](/docs/SDK/Source/Classes/structFDialogHandle.md) | **[[ShowNoButtonsWorkingDialog]]**(FText Title, FText Body, int32 DialogPriority) |
| [FDialogHandle](/docs/SDK/Source/Classes/structFDialogHandle.md) | **[[ShowOkCancelDialog]]**(FText Title, FText Body, FDialogButtonDelegate OkDelegate, FDialogButtonDelegate CancelDelegate, int32 DialogPriority) |
| [FDialogHandle](/docs/SDK/Source/Classes/structFDialogHandle.md) | **[[ShowOkDialog]]**(FText Title, FText Body, FDialogButtonDelegate OkDelegate, int32 DialogPriority) |
| [FDialogHandle](/docs/SDK/Source/Classes/structFDialogHandle.md) | **[[ShowYesNoDialog]]**(FText Title, FText Body, FDialogButtonDelegate YesDelegate, FDialogButtonDelegate NoDelegate, int32 DialogPriority) |
| | **[[UTBLDialogManager]]**() |

## Protected Functions

|                | Name           |
| -------------- | -------------- |
| void | **[[PushDialog]]**([UTBLDialogWidget](/docs/SDK/Source/Classes/classUTBLDialogWidget.md) * Dialog, int32 DialogPriority) |

-------------------------------

Updated on 2023-07-04 at 02:31:00 +0200