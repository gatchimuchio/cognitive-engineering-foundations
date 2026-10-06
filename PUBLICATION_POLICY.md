# 公開・言語・命名・理論状態ポリシー
## Publication / Language / Naming / Theory-State Policy

**版**：v1.3.4  
**改訂日**：2026-10-07  
**著者**：がっちむち♂  
**規定言語**：日本語  

本書は `cognitive-engineering-foundations` における現行公開方針を規定する。

旧リポジトリ名 `closure-phase-specs` は履歴上の名称としてのみ扱い、現行名称として使用しない。

---

# 1. 日本語を基底・規定言語とする

本理論群では、日本語を唯一の基底言語・規定言語とする。

```text
日本語で理論生成
→ 日本語で定義・構造化
→ 日本語で監査・改訂
→ 日本語原典成立
→ 実務上必要な場合のみ多言語へ翻訳
```

多言語版は日本語原典から生成された翻訳・射影であり、独立した正本ではない。

多言語部は、その実体に応じて次を明示する。

- **Translation**：日本語原典と節・意味を対応させた全文翻訳
- **Summary Projection**：日本語原典から要点を抽出した要約射影

要約を `Translation` と表示してはならない。現行00〜08の英語部は、全文対訳ではなく **English Summary Projection** として扱う。

意味が衝突した場合、日本語原典を優先する。

翻訳時に未定義・意味衝突・関係欠落・説明不足が見つかった場合、翻訳側で勝手に補完せず、日本語原典を先に再監査・改訂する。

---

# 2. 多言語使用条件

英語その他の言語は、国際公開、外部規格、API、応募、共同作業その他、実務上必要な場合に限って使用する。

「国際公開するから最初から英語で原典を作る」という順序は採用しない。

---

# 3. 共通理論状態

本リポジトリの現行公開理論は、共通して次の状態で記述する。

## 3.1 時点付きProjection

定義、対象、主体、関係、文脈、時間、空間、因果、価値、評価、観測、モデル、原理、規則、判断、理論自身を、認知以前から固定された最終実体として扱わない。

各文書は、その版・時点・目的・観測範囲における現行Projectionである。

## 3.2 版内固定

暫定であることを理由に、同一版の意味を無言変更してはならない。

現行版内部では監査可能性のために、必要な定義・対象・関係・境界・判定を明示的に固定する。

変更する場合は新しい版で行い、旧版を保持する。

## 3.3 局所閉包／全体開放

特定Case・特定目的・特定時点では、判断・実装・断定のために強く局所閉包してよい。

ただし、局所閉包を世界全体・将来全体・理論全体の最終閉包へ昇格させない。

```text
Local closure = allowed
Global final closure = not claimed
```

## 3.4 暫定は弱さではない

「暫定」は、弱い、任意、同価値、変更自由、判断不能を意味しない。

現在条件で強く成立するものは強く採用してよい。

ただし、現在の強度を永久不可侵性へ変換しない。

## 3.5 時間軸上の全体再開放

新観測・時間経過・実装結果は、既存モデルの値だけでなく、

- 主体
- 対象
- 主体／対象の区別
- 対象同一性
- 関係
- 文脈
- 時間・空間・因果
- 目的・価値・評価規則
- 定義・前提・射程
- 観測方法
- 理論記述
- 過去判断の意味

を変え得る。

必要なら、結果だけでなく問い・対象・座標・理論そのものへ戻って再構成する。

## 3.6 旧版を上書きしない

過去版は、当時の認知・観測・言語・目的における記録として保存する。

新しい版が旧版の意味を再解釈する場合も、旧版本文を遡及改変せず、新旧対応を新しい版側に記録する。

## 3.7 自己適用

各理論は、自分自身を自分の監査対象から外してはならない。

- 認知工学は認知工学自身の定義を監査する。
- 言語基底論は自分の語彙圧縮を監査する。
- 旨味ギャップは自分自身が欠落変数を作っていないか監査する。
- トリニティ原理は「世界は3で閉じる／3が世界構築の最小構造」という三項最小性を現行原理命題として保持しつつ、X / R / Mを唯一絶対の表現へ固定しない。
- 閉包位相Ψは「安定」という自分の観測語を固定実体化しない。
- 神の領域原理（仮）は自身を最終真理へ固定しない。
- 意識論は、意識・主観・自我・三観測チャネル・外界拘束という現在の分別を固定実体化せず、構造記述と起動因果を分離する。
- 適用論文は監査器・ゲーム世界等の自分の切り出しを再監査する。

## 3.8 原理・対象と有限記述の非同一

理論、原理、対象、現象と、それらを言語・記号・数式・図・コードで記述した有限文書を同一視しない。

現行文書は公開可能な有限Projectionであり、対象総体を完全同型に回収したとは宣言しない。

## 3.9 主張種別の分離

本文中の記述は、必要に応じて次の種別を区別する。

- **規定・定義**：本体系または当該版が採用する意味・境界・運用条件
- **観測**：ログ、実験、実装結果、直接確認された事実
- **外部事実**：外部一次資料等で確認する事実
- **推論**：観測・定義・前提から導出した解釈
- **仮説**：現時点で候補として保持する説明
- **未確認・未知**：確認できていない事項、残差

規定を観測事実として扱わず、仮説を確定事実へ昇格させず、外部事実を権威による理論証明へ転用しない。

## 3.10 Projection責任原則

有限記述と原理・対象を非同一とすることは、現行版の反証逃れを許可しない。

> **現行Projectionが、その版自身の宣言した射程・条件・定義の内部で反証された場合、当該版の該当主張はFAILまたは改訂対象として記録する。**

「反証されたのは文章であり原理そのものではない」という未観測領域を、現行版の救済根拠にしてはならない。

更新する場合は、新しい版として、旧版・反証点・変更理由・影響範囲・保持事項を追跡可能にする。

## 3.11 停止状態の型分離

「分からない」「仕様に反する」「利用境界を越える」「実行系が壊れた」を同じ停止状態へ潰さない。

原則として次を区別する。

- **PASS / ASSERT**：現行目的に必要な局所閉包が成立
- **SUSPEND**：未観測・未閉包・未定義・決定不能等の認識上の保留
- **REJECT**：定義矛盾・仕様違反等による論理／仕様上の拒否
- **OUT-OF-SCOPE**：倫理・公開・適用境界により処理対象外
- **FAIL**：Runtime、API、実行環境、ログ欠損等の運用障害

各論文は必要な部分集合を採用してよいが、意味の異なる停止理由を無言で同一化しない。

---

# 4. 公開粒度

本理論群の公開文書は、上記の理論状態を理解できる粒度まで記述する。

少なくとも、必要に応じて次を明示する。

- 現行定義
- 現行射程
- 時点・条件
- 局所閉包の意味
- 世界本体への非昇格
- 再開放条件
- 自己適用
- 旧版との関係

ただし、公開粒度を上げることと、非公開理論の内部構造を公開することは同じではない。

HDSについては第7章の公開境界を優先する。

---

# 5. 正式名称

## 5.1 神の領域原理（仮）

```text
正式名称：神の領域原理（仮）
略称：神域原理（仮）
```

英語環境でも日本語名を正式名として保持する。

`（仮）` は、本原理自身を最終真理へ固定しない構造的暫定性を示すため保持する。

## 5.2 トリニティ原理

```text
正式名称：トリニティ原理
英語説明：Trinity Principle
```

`（仮）` は付さない。

## 5.3 閉包位相Ψ

```text
正式名称：閉包位相Ψ
英語説明：Closure Phase Ψ
```

`（仮）` は付さない。

## 5.4 HDS

```text
正式名称：Human Decision-making System（仮）
和名：人間意思決定理論（仮）
略称：HDS
```

`（仮）` を保持する。

## 5.5 意識論

```text
正式名称：意識論
英語説明：Theory of Consciousness
```

`（仮）` は付さない。

本稿でいう意識論は、意識・主観・自我を固定内面実体として断定する理論ではなく、外界拘束・自己／非自己・認知・メタ認知・一人称的制御原点・時間安定結果を分別する現行公開Projectionである。

---

# 6. （仮）の適用範囲

本理論群で `（仮）` を名称に付すのは、原則として次の二系統のみである。

1. 神の領域原理（仮）／神域原理（仮）
2. Human Decision-making System（仮）／人間意思決定理論（仮）

その他の理論名には、個別の明示指示がない限り `（仮）` を付さない。

---

# 7. HDS公開境界

HDSについて現行公開範囲に含める情報は、原則として名称のみである。

公開可：

```text
Human Decision-making System（仮）
人間意思決定理論（仮）
HDS
```

現行公開範囲外：

- 内部構造
- 相・層・ループ
- 判断機構
- 評価設計
- 運用手順
- 実装
- 再現可能なレシピ
- 内部パラメータ・閾値・検出器
- その他、名称を超えて内部作用を再構成できる情報

本リポジトリの他理論をHDSと同じ理論状態・認識粒度へ揃える場合も、HDS内部構造を類推・転記・再現する形では行わない。

旧版に詳細記述が存在する場合、その記述は歴史資料として `archive/` に保存し、現行仕様として扱わない。

---

# 8. root と archive の分離

リポジトリrootには現行公開正本だけを置く。

旧版、旧名称、旧読書順、旧適用例、旧ツールは `archive/` へ退避する。

```text
root    = current canonical public set
archive = historical / superseded set
```

archive 内の記述は、当時の状態を保持するため原則として無言修正しない。

旧称 `closure-phase-specs` を含むarchive内文書は、改称前の歴史状態として保持する。

---

# 9. 版更新

理論の意味・状態・粒度が変化する更新は版番号を上げる。

版更新では、可能な範囲で、

- 何が変わったか
- なぜ変わったか
- どの旧結論へ影響するか
- 何を現在も保持するか
- 何を再開放したか

を追跡可能にする。

現在の正本を過去版へ無言上書きしない。

---

# 10. 著者表記

公開文書の著者表記は、原則として次に統一する。

```text
がっちむち♂
```

英語翻訳部でも著者名を置換しない。

---

# 11. 参照文献の位置づけ

外部参考文献は、座標合わせ、既存用語、歴史的背景、工学上の隣接概念を確認するために利用する。

本理論群の正しさを権威によって証明するためのものではない。

---

# 12. 適合条件・利用境界と著作権ライセンスの分離

本文中の誓約、禁止、OUT-OF-SCOPE、利用境界は、本理論群に「適合する」と名乗るための意味上・倫理上・運用上の条件である。

これらを、CC BY 4.0 が与える著作権上の許諾へ追加の法的制限を課す条項として扱わない。

```text
copyright license = LICENSE
theory conformance / ethical boundary = each specification
```

したがって、ライセンス上許可される再利用であっても、本理論群の適合条件を外れた派生物は「神の領域原理（仮）／トリニティ原理／HDS等に適合する実装」とは扱わない。

---
# 13. 現行正本順

```text
00_認知工学とは何か_v0_4_ja_en.md
01_情報工学における言語基底論_v0_4_ja_en.md
02_Umami_Gap_v1_3_ja_en.md
03_トリニティ原理_v1_2_ja_en.md
04_閉包位相Ψ_v1_2_ja_en.md
05_神の領域原理（仮）_v1_3_ja_en.md
08_意識論_v0_1_ja_en.md
06_トリニティ原理適用_論証監査_v0_5_ja_en.md
07_トリニティ原理適用_ゲーム理論と均衡_v0_7_ja_en.md
```

---

# English Translation

## Publication / Language / Naming / Theory-State Policy

This policy governs the current public repository `cognitive-engineering-foundations`. The former name `closure-phase-specs` is historical only.

Japanese is the sole base and normative language. Originals are established in Japanese before any downstream translation.

All current public theories use a common theory state:

- time- and version-bounded Projection;
- version-local fixation for auditability;
- strong local closure without global finalization;
- provisionality that does not mean weakness or arbitrariness;
- reopening of targets, relations, definitions, evaluation axes, and past interpretations when material new observation requires it;
- preservation of older versions rather than retroactive overwrite;
- self-application;
- separation between a theory or target and its finite written description.

Public documents should expose this theory state at sufficient conceptual resolution, but this does not authorize disclosure of non-public HDS internals.

Canonical names:

```text
神の領域原理（仮） / 神域原理（仮）
トリニティ原理 / Trinity Principle
閉包位相Ψ / Closure Phase Ψ
意識論 / Theory of Consciousness
Human Decision-making System（仮）
人間意思決定理論（仮）
HDS
```

Only 神の領域原理（仮） and HDS carry `（仮）` as part of their current names.

For HDS, only the names are public. Internal structure, phases, loops, evaluation design, operation, implementation, reproducible recipes, thresholds, and equivalent reconstructive details remain outside the public scope.

Older public repositories or demos that contain historical HDS projections are legacy artifacts, not current HDS specifications. Their public availability does not expand the current disclosure boundary.

The repository root contains only current canonical public documents. Superseded material is stored under `archive/`.
