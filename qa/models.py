from django.db import models

class Question(models.Model):
    # Champ pour stocker la question
    question_text = models.TextField()
    
    # Champ pour stocker la réponse, ce champ est optionnel
    answer_text = models.TextField(blank=True, null=True)
    
    # Champ pour enregistrer la date et l'heure de création de la question
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # Retourne les 50 premiers caractères de la question
        return self.question_text[:50]

    class Meta:
        # Tri des questions par date de création décroissante (les plus récentes en premier)
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        # Vous pouvez ajouter des logiques supplémentaires avant l'enregistrement, par exemple :
        # Si la réponse est vide, la définir à 'Pas encore répondu'
        if not self.answer_text:
            self.answer_text = "Pas encore répondu"
        super().save(*args, **kwargs)
