"""Contoh file yang MELANGGAR standar (untuk demo pre-commit hooks)."""
import sys
import os
import pandas


def hitung( x,y ):
    z=x+y
    print( "hasil:",z )
    return z

hitung( 1,2 )
