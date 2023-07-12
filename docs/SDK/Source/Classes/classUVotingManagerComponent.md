---
title: UVotingManagerComponent
type: class
aliases: UVotingManagerComponent
share: false

---

# UVotingManagerComponent





Inherits from UActorComponent, [IReplicatedSubobjectInterface](/docs/SDK/Source/Classes/classIReplicatedSubobjectInterface.md)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| bool | **[[CanVoteStart]]**([ATBLPlayerController](/docs/SDK/Source/Classes/classATBLPlayerController.md) * VotingController, FName VoteOption, [UVotingInstance](/docs/SDK/Source/Classes/classUVotingInstance.md) * VotingInstance) |
| virtual void | **[[GetLifetimeReplicatedProps]]**(TArray< FLifetimeProperty > & OutLifetimeProps) const override |
| int32 | **[[GetNumValidInstancesForClass]]**(TSubclassOf< [UVotingInstance](/docs/SDK/Source/Classes/classUVotingInstance.md) > VoteClass, [ATBLPlayerController](/docs/SDK/Source/Classes/classATBLPlayerController.md) * VotingController) |
| int32 | **[[GetNumVoteInstancesForClass]]**(TSubclassOf< [UVotingInstance](/docs/SDK/Source/Classes/classUVotingInstance.md) > VoteClass) |
| | **[[UVotingManagerComponent]]**() |

## Protected Functions

|                | Name           |
| -------------- | -------------- |
| void | **[[BroadcastVoteFinished]]**(const [FVotingResults](/docs/SDK/Source/Classes/structFVotingResults.md) & VoteResults) |
| void | **[[RemoveInstance]]**([UVotingInstance](/docs/SDK/Source/Classes/classUVotingInstance.md) * VotingInstance) |
| void | **[[VoteFinished]]**(const FName & VoteResult) |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| [FReplicatedArray_UVotingInstances](/docs/SDK/Source/Classes/structFReplicatedArray__UVotingInstances.md) | **[[VotingInstances]]**  |

## Protected Attributes

|                | Name           |
| -------------- | -------------- |
| FVoteFinishedSignature | **[[OnVoteFinished]]**  |
| TSet< TSubclassOf< [UVotingInstance](/docs/SDK/Source/Classes/classUVotingInstance.md) > > | **[[ValidInstances]]**  |

-------------------------------

Updated on 2023-07-04 at 02:31:01 +0200