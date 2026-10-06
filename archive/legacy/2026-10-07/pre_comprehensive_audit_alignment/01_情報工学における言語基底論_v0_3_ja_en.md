# 情報工学における言語基底論
## ― 認知によって生成される情報を、いかに効率よく保持・操作・継承するか ―

**版**：v0.3  
**著者**：がっちむち♂  
**文章生成支援**：LLM  
**原典言語**：日本語  

> **言語規定**：本稿は日本語原典を正本とする。英語版は日本語原典成立後に作成された翻訳であり、意味が衝突する場合は日本語原典を優先する。

> **理論状態規定**：本稿の「情報」「情報工学」「意味構造保持効率」「言語基底」「日本語基底」という定義・分類・評価は、v0.3時点の認知世界・目的・観測範囲における現行Projectionである。現行版内部では強く採用するが、最終存在論・永久不変の言語順位へ固定しない。

---

# Part I. 日本語原典

## 1行定義

> **情報工学における言語基底とは、認知によって生成された情報を、意味・関係・文脈・状態・未確定性を可能な限り失わず、効率的に保持・操作・再利用するための基礎表現系である。本稿は、この目的に対して日本語を基底言語として採用する。**

---

# 0. 本稿の理論状態

本稿は、

```text
世界
↓
認知
↓
情報
↓
情報操作
```

という現在の構造理解から出発する。

しかし、この順序を認知以前の世界本体の最終階層として宣言しない。

本稿で「情報は認知の産物である」と言うとき、v0.3の現行定義では強くそのように採用する。一方で、将来、認知・情報・主体・対象・外界の区別そのものを再構成する新観測が得られれば、情報の定義から再開放する。

同様に、日本語基底は「永遠に日本語が最強である」という宣言ではない。

> **現在の対象・目的・意味構造保持要求に対して、日本語を基底言語として強く採用する版内設計判断である。**

再開放時には、言語だけを差し替えるのではなく、

- 何を情報とみなすか
- 何を損失とみなすか
- 何を意味構造保持とみなすか
- どの認知主体・用途・時間軸を対象としているか
- どの比較軸を用いたか

まで上流へ戻って監査する。

「暫定」は任意変更を意味しない。現行条件では日本語基底を規定として固定し、変更には現行判断を崩す具体的な観測・実装結果・構造変化を要求する。

---

## 要旨

情報は世界にそのまま存在する物ではない。

世界に何らかの差異や作用が存在するとしても、それが「情報」として成立するためには、認知主体による検出、対象化、差異化、関係化、意味づけ等を必要とする。

したがって、

> **情報は認知の産物である。**

本稿の現行基本関係は、

```text
世界
↓
認知
↓
情報
↓
情報の操作
```

である。

この構造から、本稿はv0.3の現行定義において「情報科学」を独立した Science として採用しない。情報は認知より下流で成立する認知後生成物であり、その記録・符号化・保存・伝送・検索・変換・結合・計算・再利用は、情報をどう扱うかという目的付きの操作・設計問題である。したがって本稿では、その営みを**情報工学**として扱う。

情報工学の性能は、単なるbit数、通信速度、圧縮率、計算速度だけでは決まらない。認知によって成立した意味・関係・文脈・差異・未確定性を、次の処理までどれだけ壊さず運べるかも重要である。本稿はこれを**意味構造保持効率**と呼ぶ。

人類がこの目的のために長期間使用してきた主要な情報操作基盤が言語である。言語は会話手段にとどまらず、認知結果を外部化し、名前を与え、差異を保存し、関係を記述し、時間を越えて保存し、他者や次世代の認知へ再入力する情報工学基盤である。

本稿は、この目的において日本語の構造を評価する。日本語は、漢字・かな・助詞・活用・語尾・省略・文脈等を同一記述面で併用し、意味・関係・態度・共有状態・未確定性を複数層として保持できる。この特徴は、本理論群が要求する理論生成・構造化・監査・再利用に高い適合性を持つ。

したがって本理論群では、

> **日本語を唯一の基底言語・規定言語とし、日本語原典を先に成立させ、実務上必要な場合のみ後段で他言語へ翻訳する。**

---

# 1. 情報とは何か

世界に光、音、物体、変化があるとしても、本稿はそれらを存在するだけで「情報」とは呼ばない。

認知主体が何かを検出し、他と区別し、対象として切り出し、状態を認識し、他の対象と関係づけ、意味を与えることで、その差異は主体が扱える情報になる。

したがって本稿では、

> **情報とは、認知によって世界から切り出され、主体が操作可能な状態へ変換されたもの**

と定義する。

この定義はv0.3の版内定義である。「主体」「世界」「認知」「意味」「操作可能」という各語も固定実体ではない。新しい観測によってそれらの区別が変わるなら、情報定義そのものを再構成する。

---

# 2. 「情報科学」はなぜ成立しないのか

前稿『認知工学とは何か』で分別した通り、Science は観測可能な現象・作用・関係について何が成立しているかを観測する営みであり、Engineering は目的を置き、対象へ作用し、目的状態を実現する営みである。

情報は認知によって成立した後段の対象である。

一般に「情報」の名の下で行われる主要な営みは、符号化、記録、保存、圧縮、伝送、検索、分類、変換、計算、結合、推論、再利用等である。

これらは、

> **情報をどう扱うか**

という操作・設計問題である。

したがって、

> **本稿はv0.3の現行定義において「情報科学」という独立した Science を認めない。**

既存の「情報科学」という名称の下で行われている個々の有用な研究・技術を否定するものではない。否定するのは分類である。

認知によって生成された情報を目的に応じて扱う営みは、原理的には**情報工学**である。

この判断も再監査対象だが、根拠のない可能性留保で現行判断を薄めない。再開放には、情報の成立位置またはScience / Engineeringの成立条件を変える具体的な再分別を要求する。

---

# 3. 認知科学への批判との違い

認知科学への批判と情報科学への批判は同じではない。

認知科学の問題は、

> **直接観測できない認知そのものを、認知後の外部現象から構築したモデルによって Science の対象として扱えるのか。**

という問題である。

情報科学の問題はさらに下流にある。

> **その認知によって生成された情報が、なぜ独立した Science の対象たり得るのか。**

という問題である。

```text
世界
↓
認知       ← 認知科学の成立問題
↓
情報       ← 情報科学の成立問題
↓
情報操作   ← 情報工学
```

この図自体も現行説明Projectionである。重要なのは、二つの批判の成立位置を混同しないことにある。

---

# 4. 情報工学とは何をするのか

情報工学の目的は、情報を独立した存在論的実体として説明することではない。

> **認知によって成立した情報を、目的に応じて、損失少なく、効率的に扱うこと。**

である。

したがって性能には、単純な処理速度だけでなく、次も含まれる。

- 必要な意味が保持されているか
- 対象間の関係が保持されているか
- 文脈が保持されているか
- 元の差異が潰れていないか
- 未確定なものが勝手に確定されていないか
- 後から再解釈できるか
- 別用途へ再利用できるか

本稿ではこれらをまとめて、

> **意味構造保持効率**

と呼ぶ。

ただし「意味」「構造」「保持」「効率」という評価軸も、用途・主体・時間・実装によって変わり得る。したがって比較軸そのものを将来の監査から免除しない。

---

# 5. 情報量と意味構造保持効率は別である

bit数、圧縮率、通信速度、計算速度は重要である。しかし、それだけでは認知によって生成された情報の取り扱い効率を評価できない。

極端に短い記号で巨大な概念を参照できても、その概念を再構成できなければ意味処理として成立しない。

逆に、すべてを長文で逐一展開すれば明示性は増えるが、常に巨大な再展開を要求するなら操作効率は低い。

したがって重要なのは、

> **圧縮された状態でも必要な意味構造を保持し、必要なときに再展開できること。**

である。

本稿でいう効率は、通信路上の情報量だけを指さない。

---

# 6. 言語は情報操作基盤である

言語は単なる会話手段ではない。

言語は、認知結果を外部化し、対象へ名前を与え、差異を保存し、関係を記述し、状態を共有し、過去の認知を未来へ保存し、他者の認知へ入力し、複数の情報を組み合わせ、新しい認知を生成する。

したがって、

> **言語は、人類が構築した巨大な情報工学基盤である。**

文明規模の情報継承には、口頭運用だけでなく記録運用が必要になる。

なお、文字以前の口語を直接観測することはできない。口語が文字より先に存在したという理解は自然な推論であるが、文字以前の音声そのものを現在直接参照できるという意味での観測事実ではない。本稿はこの区別を維持する。

---

# 7. 日本語の構造

本稿では、日本語を単純な単一系統の表音言語として扱わない。

現代日本語では、大和言葉を中心とする口語的系譜、漢字・漢文を通じて取り込まれた意味記述・概念記録の系譜、かなによる日本語音声・文法の記録、漢語・和語・外来語の多重運用が重なっている。

歴史的起源の全てを本稿で一意に固定することは目的ではない。

重要なのは現在観測できる構造である。

> **日本語は、意味差を強く保持する記号と、音・作用・関係・状態を記述する記号を同一文中で併用できる。**

この混成性を、本稿では情報処理能力として評価する。

ただし「日本語」という対象境界自体も歴史的・時間的に変化する。現代日本語の現在構造を、過去・未来の全日本語へ無条件に拡張しない。

---

# 8. 漢字とかな

漢字は単純な「一文字一意味」ではない。しかし日本語運用では、音だけでは重なる語・概念を記述段階で分離する強い働きを持つ。

例えば、

```text
意思
意志
医師
```

は同音でも、文字によって別の意味スロットとして保持される。

かなは音を記録するだけではない。助詞、活用、語尾、接続、状態変化、話者態度等を担い、関係情報の保持へ作用する。

本稿の比較モデルでは、日本語文は概略として、

> **漢字側に意味・概念の核を置き、かな側に関係・作用・状態を流す。**

という多層記述を可能にする。

これは厳密な一対一規則ではなく、情報工学上の現行構造傾向として扱う。

---

# 9. 文脈は必ずしも欠落ではない

明示されていない情報を、すべて欠落とみなすことはできない。

共有文脈内に保持され、必要に応じて再構成可能であれば、それは単純な情報消失ではない。

コンピュータで言えば、毎回全状態を送信するのではなく、既存状態を参照しながら差分を操作する方式に近い。

日本語では主語や対象を省略できる。文脈が共有されていなければ誤認を生むが、共有文脈が成立している条件では、既知情報を繰り返さず、新しい差分だけを伝達できる。

これは情報工学的には圧縮として機能し得る。

---

# 10. 未確定性を保持する

情報処理において、常に早く明確化することが最適とは限らない。

未観測、複数解釈、現時点で判断不要、将来入力によって変化する項目を早期に一つへ固定すると、情報が増えるのではなく可能性空間を削除する。

日本語は、主体・確定度・態度・因果等の一部を、必要になるまで文脈内に保持する運用と相性がよい。

本稿はこの性質を、

> **未確定性保持能力**

として評価する。

この評価も言語・用途・観測主体に依存する現行判断であり、普遍的な一軸性能へ固定しない。

---

# 11. 英語との比較

英語は、国際規格、API、ソフトウェア、技術文書、学術流通、国際共同作業において極めて強い実務基盤である。

本稿は英語の使用を否定しない。

しかし、

> **外部接続に強いこと**

と、

> **理論・概念を最初に生成する基底として意味構造を保持しやすいこと**

は別の評価軸である。

本稿の比較モデルでは、英語はアルファベットによる線形記述を中心とし、細かな意味差・関係差を保持する際に、語彙選択、語順、修飾、説明追加等による明示展開を要求しやすい。

日本語は、漢字、かな、助詞、活用、省略、文脈等へ異なる情報を分散できる。

したがって本稿では、目的を限定した上で、

> **英語は外部接続に強く、日本語は内部意味構造の保持に強い。**

という役割差を置く。

これは人間・民族・文化の優劣評価ではない。情報工学上の基底表現に対する目的適合評価である。

比較対象の言語状態、利用者、LLM、記述媒体、目的が変われば、この比較結果も再監査する。

---

# 12. 「12色と36色」の比喩

本稿では、言語の差を説明するために「12色の絵具と36色の絵具」という比喩を用いる。

これは日本語の語彙数が英語の3倍だという数量主張ではない。

同じ最終色を作れるとしても、初期スロットが少ない系では複数状態を混合して中間色を作る必要があり、初期スロットが多い系ではより多くの中間差異を別状態のまま保持できる。

本稿が問題にするのは、

> **最終的に表現できるかではなく、情報処理途中にどの程度の差異を別状態として保持できるか。**

である。

この比喩自体も説明Projectionであり、言語能力の定量モデルではない。

---

# 13. 認知様式と言語

本稿は、言語が認知を一方向に完全決定するという単純な言語決定論を採用しない。

生成方向としては、まず、

```text
認知様式
↓
必要な情報処理形式
↓
言語の形成・選択
```

を置く。

人間集団がどの差異を重視し、どう関係を認識し、何を記録する必要があったかが、言語形成へ作用したと考える。

一度言語が成立し継承されると、今度はその言語が次世代の認知操作へ作用する。

```text
認知
↓
言語
↓
継承
↓
認知
↓
言語
↓
……
```

したがって、認知と言語は再帰的に自己強化し得る。

この因果記述も現行モデルであり、認知と言語の境界・順序・相互作用について新観測が得られれば再構成する。

---

# 14. LLM時代の言語分業

従来、最終公開先が英語であるなら、最初から英語で論文・仕様を生成する実務圧力が存在した。

LLMによって、翻訳、対訳、文体変換、用語固定、翻訳差分監査のコストは大幅に低下した。

その結果、

> **理論を生成する言語**

と、

> **外部へ公開する言語**

を同一にする必要性は低下した。

最も意味構造を保持しやすい言語で原典を成立させ、その後、必要な出力先へ変換すればよい。

この技術条件が変われば、言語分業の合理性も再監査する。

---

# 15. 日本語基底規定

本理論群では次を規定する。

1. **日本語を唯一の基底言語・規定言語とする。**
2. **原典は必ず日本語で先に成立させる。**
3. 英語その他の言語は、国際公開、規格、API、応募、共同作業その他、実務上必要な場合にのみ使用する。
4. 多言語版は日本語原典から生成された翻訳・射影であり、独立した正本としない。
5. 翻訳で未定義・意味衝突・関係欠落・説明不足が発見された場合、翻訳側で勝手に補完せず、日本語原典を再監査・改訂してから再翻訳する。

運用順序は次である。

```text
日本語で認知・思考
↓
日本語で理論生成
↓
日本語で定義・構造化
↓
日本語で監査
↓
日本語原典成立
↓
必要な場合のみ他言語へ翻訳
↓
日本語原典との意味差監査
```

これは翻訳方針ではなく、

> **理論生成工程そのものの現行仕様である。**

現行版内ではこの規定を固定する。変更する場合は、基底変更だけでなく、理論生成・監査・翻訳・旧原典の意味への影響を新しい版で明示する。

---

# 16. 認知工学体系との関係

本稿は独立した言語優越論ではない。

```text
認知工学
↓
認知による世界の対象化
↓
情報の成立
↓
情報工学
↓
情報表現・操作基盤としての言語
↓
日本語基底
```

という位置にある。

この関係図自体も現行Projectionであり、最終世界階層ではない。

本認知工学体系には、**神の領域原理（仮）**、**トリニティ原理**、**閉包位相Ψ**が存在する。

また、次の名称が存在する。

```text
Human Decision-making System（仮）
人間意思決定理論（仮）
HDS
```

本稿でHDSについて公開するのは名称のみである。

---

# 17. 時間軸・再開放条件

日本語基底規定は強い現行設計判断であるが、永久不可侵ではない。

少なくとも次の場合、本稿は上流から再監査する。

- 日本語より高い意味構造保持効率を持つ記述系が成立した
- 日本語固有の認知固定が重大な取り零しを生んだ
- 自然言語以外の中間表現がより適合した
- LLM・記録媒体・翻訳環境の変化で基底／出力分離の合理性が変わった
- 「情報」「意味」「保持」「効率」という比較軸自体が不十分と判明した
- 認知と情報の現在関係を変更する観測が得られた

再開放時には、過去版を誤りとして消去せず、当時の対象・目的・比較条件に対する記録として保持する。

---

# 18. 自己適用

本稿は、言語が差異を保持する能力を論じている。

したがって本稿自身が、現在の用語によって差異を潰していないかを監査対象にする。

例えば、

- 「日本語」
- 「英語」
- 「表意／表音」
- 「意味構造」
- 「情報」
- 「文脈」

という大きな語が、内部の異なる構造を一語へ圧縮している可能性を常に残す。

> **言語論そのものが新しい旨味ギャップを作っていないかを監査する。**

---

# 19. 非目標

本稿は、日本人・日本民族・日本文化が他者より優れているとは主張しない。英語で高度な思考が不可能だとも主張しない。日本語が常に最少トークン・最高通信速度になるとも主張しない。

評価対象は限定されている。

> **認知によって生成された情報を、理論生成・構造化・監査・再利用する基底表現としての適合性。**

である。

---

# 20. 結論

情報は世界にそのまま置かれている物ではない。

> **世界 → 認知 → 情報**

である。

認知によって成立した情報を保存・伝達・変換・計算・検索・結合・再利用する営みは、Science ではなく Engineering である。

したがって本稿はv0.3の現行定義において「情報科学」を採用せず、**情報工学**として扱う。

言語は、人類が認知によって生成した情報を外部化・保存・伝達・再入力する巨大な情報工学基盤である。

日本語は、漢字による意味差の保持、かなによる音・作用・関係の記述、助詞・活用・語尾による関係情報、文脈による共有状態参照、未確定性の保持、複数文字体系・語彙系統の同時運用を一つの記述面で扱える。

この構造は、本理論群の意味構造保持効率という現在目的に高く適合する。

よって、

> **日本語を基底言語・規定言語として採用する。**

この結論は強く運用する。ただし、日本語・情報・認知・比較軸・理論生成環境そのものを将来の再監査から免除しない。

---

# Part II. English Translation

# A Theory of Language Bases in Information Engineering
## Efficiently Preserving, Operating on, and Inheriting Information Generated by Cognition

**Version**: v0.3  
**Author**: がっちむち♂  
**Writing assistance**: LLM  
**Authoritative language**: Japanese

> The Japanese original above is authoritative. This English translation is downstream of that original.

## Theory-state rule

The current relation `World → Cognition → Information → Information Operation`, the rejection of “Information Science,” the metric of semantic-structure preservation efficiency, and the Japanese-base rule are current v0.3 Projections. They are strongly adopted inside this version but are not promoted into final ontology or permanent language ranking.

Reopening a language decision requires reopening its upstream conditions when necessary: what counts as information, loss, semantic structure, target agent, purpose, and comparison axis.

“Provisional” does not mean arbitrary. Japanese remains the normative base language under the current conditions until material evidence or structural change justifies revision.

## Information

Information is currently defined as what cognition cuts out from the world and transforms into an operable state for an agent. The terms agent, world, cognition, meaning, and operability are themselves version-bounded and may be reconstructed under new observation.

## Information Science / Information Engineering

Under the current Science / Engineering distinction, this paper does not recognize Information Science as an independent Science. Encoding, storing, transmitting, searching, transforming, computing, combining, inferring, and reusing cognitively constituted information are treated as Information Engineering.

This judgment remains reopenable but is not weakened by unsupported possibility language.

## Semantic-structure preservation efficiency

Efficiency includes preservation of meaning, relation, context, differences, unresolvedness, reinterpretability, and reusability—not only bit count, compression ratio, transmission speed, or compute speed.

The metric itself is also a current evaluation Projection and may be revised if the purpose or cognitive frame changes.

## Japanese as the base language

Japanese is selected because its combined use of kanji, kana, particles, inflection, omission, and context can preserve multiple semantic and relational distinctions on one descriptive surface.

The present role distinction is:

> **English is strong for external connection; Japanese is strong for preserving internal semantic structure.**

This is purpose-specific engineering evaluation, not ranking of people, cultures, or speakers.

## Japanese-first rule

```text
Think and generate in Japanese
↓
Define and structure in Japanese
↓
Audit in Japanese
↓
Establish the Japanese original
↓
Translate only when practically necessary
↓
Audit semantic differences against the Japanese original
```

This process is fixed inside the current version. A future change must also account for the effect on theory generation, audit, translation, and the interpretation of older originals.

## Temporal reopening and self-application

The framework is reopened if a superior representation system appears, Japanese creates material systematic omissions, a non-natural representation becomes better suited, translation technology changes the design problem, the current definition of information changes, or the evaluation axes themselves prove inadequate.

Old versions are preserved rather than overwritten.

This paper also applies its own missing-variable critique to itself: large terms such as “Japanese,” “English,” “meaning,” “information,” and “context” may compress distinctions that future versions need to separate.

## Related public theories

This Cognitive Engineering system includes **神の領域原理（仮）**, the **Trinity Principle**, and **Closure Phase Ψ**.

Only the following HDS names are public here:

```text
Human Decision-making System（仮）
人間意思決定理論（仮）
HDS
```

## Conclusion

Japanese is the current normative base language because it best fits the present engineering objective of preserving semantic structure during theory generation, structuring, audit, and reuse. The rule is strong in the present version while remaining time-bounded and reopenable at the level of its upstream assumptions.
