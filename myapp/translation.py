# myapp/translation.py

from modeltranslation.translator import translator, TranslationOptions
from .models import Category, AdStatus, Ad

class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)

class AdStatusTranslationOptions(TranslationOptions):
    fields = ('name', 'description')

class AdTranslationOptions(TranslationOptions):
    fields = () 

translator.register(Category, CategoryTranslationOptions)
translator.register(AdStatus, AdStatusTranslationOptions)
translator.register(Ad, AdTranslationOptions)
