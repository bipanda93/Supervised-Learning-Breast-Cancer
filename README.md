# 🧬 Classification ML — SVM vs KNN
### Breast Cancer Wisconsin Dataset

> Projet de machine learning supervisé comparant deux algorithmes de classification binaire pour la détection de tumeurs malignes/bénignes.

**Auteur :** Bipanda Franck Ulrich  
**Environnement :** PyCharm | Python 3 | scikit-learn  
**Date :** Février 2026

---

## 📦 Installation
```bash
pip install scikit-learn numpy pandas matplotlib seaborn
```

---

## 🗂️ Structure du Projet
```
classification-ml/
├── script1.py       # Modèle SVM
├── script2.py       # Modèle KNN
└── README.md
```

---

## 📊 Résultats

| Modèle | Meilleur paramètre | Accuracy |
|--------|-------------------|----------|
| **SVM** | C = 1 | **98.25%** ✅ |
| KNN | K = 9 | 96.49% |

---

## 🏆 Conclusion

Le **SVM (C=1 + StandardScaler)** est recommandé : 98.25% d'accuracy, 0 faux positif, seulement 2 faux négatifs.
