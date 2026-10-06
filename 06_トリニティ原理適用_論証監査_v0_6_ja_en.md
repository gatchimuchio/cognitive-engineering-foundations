# トリニティ原理適用：論証監査
## ― 自然言語の主張を、座標・関係・閉包・停止から監査する ―

**版**：v0.6  
**改訂日**：2026-10-07  
**著者**：がっちむち♂  
**文章生成支援**：LLM  
**原典言語**：日本語  

> **翻訳階層規定**：Part I = J0 日本語正本。Part II = T2 / English Summary Projection。T2は全文翻訳ではなく、独立した正本・規定文書ではない。意味衝突・欠落・曖昧さ・翻訳残差がある場合はJ0を優先し、下流側で新規主張を補わない。詳細は `TRANSLATION_POLICY.md`。

> **理論状態規定**：本稿の監査構造、X / R / M写像、PASS / SUSPEND / FAIL、反論監査、証拠強度、監査結果は、特定時点・特定目的・特定対象・特定監査者・特定文脈における現行Projectionである。監査結果を永久ラベルへ固定せず、監査器自身も監査対象から外さない。

> **Projection責任**：本版が自ら宣言した射程・条件・定義の内部で反証された場合、該当主張は本版のFAIL／改訂対象として記録する。「原理そのものは別」として現行記述を救済せず、更新は新しい版として行う。

---

# Part I. 日本語原典

## 1行定義

> **本稿は、トリニティ原理を自然言語の論証監査へ適用し、主張の表面だけでなく、対象・関係・前提・判定・停止条件が現在の目的に対して十分に閉じているかを確認するための公開適用例である。**

本稿はトリニティ原理そのものではない。

また、ここで示す層分けや監査順序を、論証監査の唯一・最終の形式として固定しない。

これは、現時点で有用な**適用Projection**である。

---

# 0. 監査結果も暫定である

監査は、固定された外部審判者が、固定された主張を永遠に裁定する行為ではない。

監査時点では、少なくとも次が現在Projectionとして成立している。

- 監査者
- 主張者
- 主張対象
- 主張同一性
- 文脈
- 時間
- 定義
- 前提
- 証拠の意味
- 反論の意味
- 評価基準
- 射程

したがって、

```text
PASS at t
≠ PASS forever
SUSPEND at t
≠ SUSPEND forever
FAIL at t
≠ FAIL forever
```

である。

ただし、暫定だから現在判定を弱めるわけではない。現在条件が十分閉じていればPASSまたはFAILを強く出してよい。

再開放時は旧判定を消さない。当時の座標と条件に対する監査記録として保持し、新しい条件で別判定を追加する。

---

## 1. 本稿の位置づけ

自然言語の主張は、文法的に完成していても、監査可能な主張として閉じているとは限らない。

例えば、

```text
AIは世界を変える。
```

という文は、意味のある発話として成立し得る。

しかし、監査対象として見ると、少なくとも次が未確定である。

- AIとは何か
- 世界とは何か
- 誰が作用主体なのか
- 何がどう変わるのか
- いつ・どこで成立するのか
- 何をもって「変わった」と判定するのか

したがって、自然言語の論証監査では、表面上の推論形式だけを見るのでは足りない。

本稿は、トリニティ原理の三項最小性を論証監査へ適用する際の代表的操作Projectionである、

```text
W_t := (X_t, R_t, M_t)
```

を監査へ適用する。

ここで、

- `X_t`：その時点で何を対象としているか
- `R_t`：対象がどう関係し、変化し、比較されるか
- `M_t`：何を同一とし、どこを境界とし、何を判定し、どこで停止するか

を扱う。

X / R / Mはトリニティ原理そのものではなく、三項最小性を論証監査へ写像した現在有効な操作Projectionである。別三項Projectionが成立しても、それだけで三項最小性そのものが崩れたとは扱わない。

---

## 2. 監査の目的

本稿の目的は、議論に勝つことではない。

目的は、

> **その主張が、現在の目的において評価・採否・反論へ進める程度に閉じているかを確認すること。**

である。

未閉包なら、無理に結論を出さない。

正当な出力として、

```text
SUSPEND
```

を許可する。

監査の目的そのものが変われば、同じ主張でも必要な閉包条件は変わり得る。

---

## 3. 最小監査構造

本稿では、論証監査を次の6つの観点へ一時的に分ける。

```text
0. 座標
1. 動態
2. 暗黙条件
3. 明示論証
4. 統合
5. 予約・SUSPEND
```

これは理解と運用のための分解であり、固定的な世界構造ではない。

必要に応じて統合・分割・追加・削除する。

### 3.1 座標

主にXを確認する。

- 誰が語っているか
- 誰が作用するか
- 何が対象か
- いつか
- どこか
- 何のための主張か

座標が定まらなければ、同じ文章でも異なる対象を読んでいる可能性がある。

同時に、「誰」「何」「いつ」という座標項目自体が足りない場合は、項目側を追加・再分別する。

### 3.2 動態

主にRを確認する。

- 初期状態
- 入力
- 変化
- 中間状態
- 分岐
- 出力
- 帰還
- 停止

結果だけが書かれ、変化経路が隠れている場合、因果や作用を監査できない。

### 3.3 暗黙条件

主にMを確認する。

- 定義
- 前提
- 射程
- 判定基準
- 未確定性
- 反証条件
- 停止条件

自然言語では、これらが読者側の常識で補完されやすい。

その補完が本文にもログにも存在しなければ、監査上は暗黙注入である。

### 3.4 明示論証

前段が閉じた後で、表面上の論証を監査する。

- 推論に飛躍はないか
- 定義は途中で変わっていないか
- 根拠は結論の強さに足りるか
- 因果と相関を混同していないか
- 比較条件は同型か

### 3.5 統合

各観点を横断し、主張が全体として安定しているかを見る。

局所的には正しくても、途中で対象・前提・評価軸が変われば、全体としては同じ論証ではない。

### 3.6 予約・SUSPEND

監査不能なもの、未観測のもの、現在の射程外にあるものは、消さずに残す。

```text
未確認
未観測
未閉包
別文脈
追加観測待ち
```

これらを、便宜的な断定で埋めない。

ただし予約項目を永久に忘却しない。新観測が来たら再び監査対象へ戻す。

---

## 4. 監査状態の型分離

### PASS / ASSERT

対象・関係・判定・停止が、現在の目的に必要な範囲で閉じている。

PASSは「世界の真理」を意味しない。

### SUSPEND

重要な対象・関係・条件・観測が不足し、結論が分岐する。認識上の保留である。

### REJECT

主張内部で定義・対象・前提・形式が破綻し、そのままでは監査対象として受理できない。

### OUT-OF-SCOPE

利用境界・公開境界・倫理境界に抵触し、監査結果とは別の理由で処理対象外とする。

### FAIL

Runtime、API、ログ欠損、実行不能等の運用障害。

```text
分からない = SUSPEND
論証／仕様が壊れている = REJECT
やらない／扱わない = OUT-OF-SCOPE
実行系が壊れた = FAIL
```

これらは時点・目的・文脈付きの状態であり、対象世界の永久属性ではない。

---

## 5. 例1：「AIは世界を変える」

```text
AIは世界を変える。
```

### X

- AIとは、モデルか、エージェントか、産業全体か
- 世界とは、経済か、技術か、制度か、生活か
- 作用主体はAIそのものか、AIを利用する人間・組織か

### R

- どの入力が
- どの仕組みを通じて
- 何を変化させ
- 何へ到達するのか

### M

- どの変化量をもって「変えた」とするか
- 期間はどこまでか
- 反例は何か
- 何が観測できれば主張を更新するか

これらが欠けたままなら、監査結果は、

```text
SUSPEND
```

である。

文章として無意味なのではない。**現在の監査目的に対して未閉包**なのである。

後日、対象・期間・作用が固定されれば、同じ文言を別の監査Caseとして再開放できる。

---

## 6. 例2：形式だけは整っている主張

```text
このシステムは効率を上げる。
効率を上げるシステムは望ましい。
したがって、このシステムは望ましい。
```

表面上は三段論法的に見える。

しかし、

- 誰にとっての効率か
- 何を効率と定義するか
- 時間軸は何か
- 副作用を含むか
- なぜ効率が望ましさへ接続するのか

が未定義なら、論証は閉じていない。

形式が整っていることと、対象・前提・評価が閉じていることは別である。

また「効率」という評価軸自体が結果観測によって不適切と判明すれば、数値だけでなく評価軸へ戻る。

---

## 7. 反論監査

反論強度は、元主張と同じ量の証拠を要求するという意味ではない。

まず主張型を確認する。

| 主張型 | 主な反証・監査条件 |
|---|---|
| 全称命題 | 射程内の有効な単一反例で崩れ得る |
| 存在命題 | 単なる非観測では通常崩れない。探索範囲の完備性、不可能性証明等を要する |
| 統計命題 | 標本、母集団、測定、効果量、不確実性、再現性を監査する |
| 因果命題 | 代替因果、交絡、介入、時間順序、反実仮想等を監査する |
| 定義・形式命題 | 定義矛盾、循環、型不一致、導出違反を監査する |
| 規範・意思決定命題 | 目的、価値、リスク、制約、不可逆性、採否規則を監査する |

したがって、

> **「元主張と同等以上の証拠量がなければ反論にならない」という一律規則は採用しない。**

例えば全称命題には一つの有効な反例が決定的になり得る。

一方、

```text
例外が存在する可能性がある。
```

という無根拠な可能性留保が、観測された強い命題を自動的に打ち消すわけでもない。

反論では、主張型、反例または反証経路、元主張のどの射程を崩すか、同じ留保を反論側へ返したとき保持されるか、証拠強度がその主張型に適合しているかを確認する。

反論側にも元主張側にも同じ型・射程・証拠規則を適用する。

---

## 7.1 三つの反論ゲート

反論を「可能性がある」「全員とは限らない」といった弱い留保だけで成立扱いしないため、次の三ゲートを通す。

## G-R1 不可能性ゲート

相手が、

> **例外が存在する可能性がある。**

と主張するなら、まず、

> **その可能性が不可能である可能性はないのか。**

を同時に通す。

ここで重要なのは、「不可能である可能性」を持ち出して相手を黙らせることではない。

狙いは、

> **片側の未観測可能性だけを、根拠なしに優先しないこと。**

である。

したがって、

```text
例外がいる可能性がある
```

だけでは反論にならない。

少なくとも、

- 具体的な候補
- 観測根拠
- 成立条件
- 既存命題のどの射程を崩すか

のいずれかを要求する。

根拠のない可能性留保を、観測事実を伴う強い命題と同列に扱わない。

---

## G-R2 反論対称性ゲート
### 別名：同型反論耐性テスト

反論を、その反論自身へ**同じ形で返したとき**、なお成立するかを見る。

例えば、

```text
傲慢でない科学者が未観測で存在する可能性がある
```

という反論を採用するなら、同型に、

```text
そのような科学者が存在しない可能性もある
```

も成立する。

前者だけを優先するなら、

> **なぜ前者だけを採用するのか、その非対称性の根拠**

を要求する。

したがって、

> **同型反論を返しただけで互いに相殺される主張は、追加根拠なしでは決着条件にならない。**

このゲートは、反論側だけでなく元主張側にも適用する。

---

## G-R3 反論強度ゲート

反論が、**元命題の型・射程・観測強度を実際に崩せるだけの強度**を持つかを見る。

ここでいう強度は、単純な証拠量ではない。

少なくとも、

- 主張型への適合
- 具体性
- 射程一致
- 観測または論理根拠
- 一貫性
- 反証経路の明示
- 元命題のどの部分を崩すか

を含む。

したがって、

```text
可能性がある
全員とは限らない
例外がいるかもしれない
```

だけでは、観測事実を伴う強い命題への反論として不足し得る。

一方で、全称命題に対する有効な単一反例のように、**証拠量は小さくても論理強度が決定的**な場合は成立する。

つまり、

```text
反論強度
≠ 証拠量の多さ
```

である。

> **必要なのは、元命題をその主張型に即して実際に崩せる強度である。**

---

## 7.2 三ゲートの適用順

反論候補R_bに対して、

```text
R_b
↓
不可能性ゲート
  片側の可能性だけを根拠なく優先していないか
↓
反論対称性ゲート
  同型で返してもなお非対称に成立するか
↓
反論強度ゲート
  元命題を主張型・射程に即して実際に崩せるか
↓
PASS / SUSPEND / REJECT
```

と扱う。

三ゲートは、反論を不可能にするための防壁ではない。

> **弱い可能性留保を、強い反証と同じ地位へ誤昇格させないための型分離である。**

---

# 8. 時間軸と監査結果の再構成

新観測は、証拠量だけを増やすとは限らない。

- 主張対象が別物だった
- 主張者と作用主体を混同していた
- 同じ語の意味が時点で変わった
- 反証とみなした事例が別スコープだった
- 評価軸そのものが不適切だった

と判明する場合がある。

その場合、古いPASS / SUSPEND / FAILを上書きしない。

> **旧判定を当時の座標に対する記録として保持し、新しい座標で再監査する。**

過去監査の意味が変わった場合は、その再解釈も別に残す。

---

## 9. 神の領域原理（仮）との接続

論証がX / R / Mの内部で閉じても、その閉じた記述が世界本体そのものになるわけではない。

したがって本適用では、最後に次を確認する。

> **その結論を、認知後に作られた記述であることを忘れて、世界本体へ誤投影していないか。**

この上位境界を担うのが、神の領域原理（仮）である。

また、神の領域原理（仮）自身も暫定Projectionであり、最終真理として固定しない。

---

## 10. 閉包位相Ψとの接続

反復監査において、対象がどのように定義を保持し、どこで停止し、どのように未確定を扱うかに安定した署名が残る場合、それを閉包位相Ψの観測対象として扱うことができる。

ただし、一回の回答、好感度、口調、人格価値からΨを断定してはならない。

また、対象・時点・観測条件が変われば、以前の安定署名をそのまま現在へ持ち越さない。

---

## 11. 自己適用：監査器を監査する

本稿は、他者の主張だけを監査して自分自身を例外にしない。

監査する。

- 6観点という分解は十分か
- PASS / SUSPEND / FAILの三状態は目的に足りるか
- 監査者の価値判断が暗黙注入されていないか
- 証拠とみなす基準が偏っていないか
- 反論強度の基準が元主張側だけに甘くなっていないか
- X / R / Mという現行Projectionを固定しすぎていないか

> **監査器が自分を監査不能にした時点で、論証監査として不整合である。**

---

## 12. 限界と再開放条件

本稿は、自然言語論証の全てを一意に評価する万能器ではない。

監査対象・目的・損失が変われば、必要な分解も変わる。

少なくとも次の場合、本稿を再開放する。

- 現行6観点で重大な取り零しが反復した
- 現行三状態では重要な差異を保持できない
- 監査者依存が結果を支配している
- 新しい論証形態・媒体・AIが現行構造を破った
- X / R / M以外の記述が高い監査性能を示した

---

## 13. 結論

自然言語の論証は、文の表面だけを見ても監査し切れない。

対象、関係、前提、判定、停止、観測範囲が暗黙のままなら、形式的に整った文章でも未閉包になり得る。

トリニティ原理を論証監査へ適用すると、まず、

```text
X_t = 何を扱うか
R_t = どう関係するか
M_t = 何をもって閉じ、どこで止めるか
```

を確認できる。

そして閉じていなければ、

```text
SUSPEND
```

を正当な出力として残す。

同時に、

> **監査結果・監査座標・監査器自身を時点付きProjectionとして保持し、条件が変われば問いまで戻って再監査する。**

これがv0.6の状態である。

---

# Part II. English Summary Projection

# Trinity Principle Application: Argument Audit
## Auditing Natural-Language Claims Through Coordinates, Relations, Closure, and Stopping

**Version**: v0.6  
**Revision date**: 2026-10-07  
**Author**: がっちむち♂  
**Writing assistance**: LLM  
**Authoritative language**: Japanese



**Translation class**: T2 / English Summary Projection  
**Source authority**: Japanese Part I / J0  
**Translation status**: CURRENT  
**Authority**: Non-authoritative and non-exhaustive. It may omit detail and must not add normative claims. In conflict, ambiguity, omission, or translation residual, Japanese Part I prevails.  
**Policy**: `TRANSLATION_POLICY.md`## Theory-state rule

The audit structure, X / R / M mapping, PASS / SUSPEND / FAIL states, rebuttal audit, evidence strength, and audit result are time-, purpose-, target-, auditor-, and context-bounded Projections.

```text
PASS at t    ≠ PASS forever
SUSPEND at t ≠ SUSPEND forever
FAIL at t    ≠ FAIL forever
```

Provisionality does not weaken a present audit. A result may be strong under current conditions while remaining reopenable when those conditions materially change.

## Current audit projection

```text
0. Coordinates
1. Dynamics
2. Tacit conditions
3. Explicit argument
4. Integration
5. Reservation / SUSPEND
```

This decomposition is operational, not final ontology.

## Typed audit states

PASS means sufficiently closed for the current purpose, not world-truth. SUSPEND means important conditions remain open. FAIL means the current claim breaks its own definitions or boundaries.

Old results are preserved if later coordinates change.

## Rebuttal audit by claim type

Rebuttal strength is claim-type dependent. A single valid counterexample can defeat a universal claim; mere non-observation usually does not defeat an existential claim; statistical, causal, formal, and normative claims require different audit conditions. The framework therefore does not impose a universal rule that a rebuttal must contain the same quantity of evidence as the original claim.
## Three rebuttal gates

Three additional gates prevent unsupported possibility language from being treated as a decisive rebuttal.

### Impossibility Gate
If a rebuttal says an exception may exist, the audit also asks whether that possibility itself may fail. The purpose is not to assert impossibility by fiat, but to prevent one-sided unsupported possibility from being privileged.

### Rebuttal Symmetry Gate
Also called the isomorphic rebuttal-resistance test. Apply the same rebuttal form back to the rebuttal itself. If both directions remain equally possible, an additional asymmetric reason is required before preferring one side.

### Rebuttal Strength Gate
A rebuttal must be strong enough to defeat the original claim under the relevant claim type and scope. Strength is not raw evidence quantity. A single valid counterexample may decisively defeat a universal claim, while vague statements such as “there may be exceptions” may be too weak to defeat a strongly observed scoped claim.

These gates apply symmetrically to the original claim and to the rebuttal.

## Temporal reconstruction

New observation may alter not only evidence but claim identity, target boundaries, meaning of terms, scope, evaluation criteria, or what counts as rebuttal.

When that happens, the older result is retained as an audit of its original coordinates and a new audit is performed.

## Rebuttal strength

Mere possibility does not automatically cancel a strongly grounded claim. Rebuttals are checked for concrete candidate exceptions, observed support, affected scope, symmetry under the same reservation, and evidential strength relative to the original claim.

Both sides remain reopenable under new evidence.

## Self-audit

The audit framework audits its own decomposition, state set, auditor dependence, evidence criteria, rebuttal symmetry, and reliance on the current X / R / M Projection of the Trinity Principle.

An audit framework that exempts itself from audit is internally inconsistent.

## Related public principles

The **Trinity Principle** supplies the core claim of triadic minimality; this paper applies its X / R / M Projection as the current local-closure audit structure. **神の領域原理（仮）** prevents closed arguments from being projected into the world-itself. Repeated stable signatures may become observation targets for **Closure Phase Ψ** under fixed conditions.

## Conclusion

The purpose of argument audit is not to maximize conclusions but to make closure and stopping inspectable. Audit results remain strong local judgments rather than permanent attributes of the world or the claim.
