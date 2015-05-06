-- Auteurs : 		   Grenier, Maxime
--	       		       Deroy, Dany
-- Codes permaments :  GREM17078606
--			           DERD02088403
-- Fichier : 		   tp1.hs
-- Date (de remise) :  20 février 2015
-- Version : 	   	   1.0
-- En utilisant uniquement les fonctions de base de Haskell 
-- (sans aucun 'import' de librairies), ecrivez les codes suivants:
--
-- Les fonctions doivent respecter le typage mentionne
-------------------------------------------------
module TP1 where

-- Ex 1 (1pt)- Donnez une fonction "verif_n" qui prend deux chaines de caracteres et un entier n en parametre, et
-- determine si le n-ieme caractere des deux chaines de caracteres est identique (sans utiliser le "if")
verif_n ::  String->String->Int->Bool
verif_n x y n = n < length x && n < length y && x!!n==y!!n

-- Ex 2(1pt)- Donnez une fonction recursive "position" qui retourne la valeur n si le n-ieme caracteres des deux chaines
-- s1 et s2 est identique, sinon la fonction retourne la valeur -1
-- exemple
	-- position "paris" "sirop" 0 => 2
	-- position "waajdi" "idja" 0 => -1
position :: String->String->Int->Int
position x y n = if x==[] || y==[] || n >= length x || n >= length y
                    then -1 
                 else if (x!!n==y!!n)
                    then n
                 else position x y (n+1)

-- Ex 3(1pts)- Ecrire la fonction recursive "inverse_chaine" qui donne l'inverse d'une chaine de caracteres (sans
-- utiliser la fonction 'reverse')
-- exemple	inverse_chaine "wajdi" => "idjaw"
inverse_chaine :: String->String
inverse_chaine x | x==[] = [] 
				 | otherwise = inverse_chaine(tail x)++[head x] 

-- Ex 4(2pts)- Ecrire la fonction recursive "partie_palyndrome" qui utilise la fonction "inverse_chaine" qui retourne
-- la partie palyndrome d'une chaine
-- exemple:	partie_palyndrome "wajdijaw" => "waj"
-- partie_palyndrome "wajdidjaw" => "wajdi"
-- partie_palyndrome "wajddjaw" => "wajd"
-- partie_palyndrome x |
partie_palyndrome :: String->String
partie_palyndrome x | (x == [] || head x /= head (inverse_chaine x)) = ""
                    | length x == 1 = x
                    | otherwise = [head x] ++ partie_palyndrome (tail (init x))

-- Ex 5(2pts)- Ecrire la fonction recursive "impaire" qui prend une liste d'entier et retourne une liste contenant
-- uniquement les impaires de lq premiere liste
-- exemple impaire [1,3,4,2] => [1,3]
impaire :: [Int]->[Int]
impaire x = if x == []
                then x
            else if (head x)`mod`2 == 1
                then [head x] ++ impaire (tail x)
            else impaire (tail x)

-- Ex 6(2pts)- Ecrire la fonction recursive "impaire_paire" qui prend une liste d'entier et retourne une liste contenant
-- les elements impaires a gauche et les elements paires a droite (NB: le rang n'est pas important)
-- exemple impaire_paire [1,2,3,4,5] => [1,3,5,4,2]
impaire_paire :: [Int]->[Int]
impaire_paire x =  if x == []
                       then x
                   else if (head x)`mod`2 == 1
                       then [head x] ++ impaire_paire (tail x)
                   else impaire_paire (tail x) ++ [head x]

-- Ex 7(5pts)- Le cryptage d'un message texte est le fait de le transformer de son format lisible et comprehensible a un
-- format incomprehensible.
-- Une facon simple de faire un cryptage est de transformer les caracteres du message en code ascii puis changer la
-- valeur de chaque code ascii en utilisant une fonction de cryptage definie, puis remettre le message crypte en format
-- texte (qui est devenu incomprehensible).
-- La pseudo-fonction a utilser pour cet exercice est la suivante : (crypter x = caractere ((code_ascii x) + y)) ou y
-- est la cle du cryptage utilisee. Etant donnee une cle = 2, le cryptage du caractere "a" va etre: caractere
-- (code_ascii "a" + 2) = caractere (97 + 2) = "c". Le decryptage ce fait en applicant la fonction inverse sur le
-- message crypte, en utilisant la meme cle de cryptage. (decrypter x = caractere ((code_ascii x) - y)). caractere
-- (code_ascii "c" - 2) = caractere (99 - 2) = "a"
-- Plus de documentation sur le cryptage : http://fr.wikipedia.org/wiki/Chiffrement

-- Creez l'application "crypter_decrypter" qui fait le cryptage et le decryptage des messages texto. L'application necessite :
	-- - le type "Transfert" qui est compose d'une cle de cryptage/decryptage de type numerique et du message a transmettre
data Transfert = Transfert (Int, String)

	-- a) (2pts) une fonction recursive "crypt" qui prend un parametre de type "Transfert" et retourne le message crypte
crypter :: Transfert -> String
crypter (Transfert x) = if snd (x) == [] then [] 
					  else [toEnum (fromEnum (head (snd x)) + fst x)::Char] ++ crypter (Transfert (fst x, tail (snd x)))

	-- b) (2pts) une fonction recursive "decrypter" qui prend un parametre de type "Transfert" et retourne le message decrypte
decrypter :: Transfert -> String
decrypter (Transfert x) = if snd (x) == [] then [] 
					  else [toEnum (fromEnum (head (snd x)) - fst x)::Char] ++ decrypter (Transfert (fst x, tail (snd x)))

	-- c) (1pt) L'application "crypter_decrypter" prend en parametre un couple de type (String, Transfert):
		-- 1er cas : si la partie "String" est "E" alors l'application "crypter_decrypter" considere que c'est un envoie
		    -- de message et par consequence lance le cryptage du message enregistre dans la partie "Transfert" en
		    -- utilisant la cle correspondante
		-- 2eme cas : si la partie "String" est "R" alors l'application "crypter_decrypter" considere que c'est une
		    -- reception de message et par consequence lance le decryptage du message enregistre dans la partie "Transfert"
		    -- en utilisant la cle correspondante
		-- 3 eme cas : autrement l'application affiche "Operation non autorisee"
crypter_decrypter :: (String, Transfert) -> String
crypter_decrypter x = if fst(x)=="E" then crypter (snd x)
						else if fst(x)=="R" then decrypter (snd x)
						else "Operation non autorisee"

-- Ex 8(6pts)- KNN (k-Nearest Neighbors) ou k plus proches voisins est un algorithme d'apprentissage supervis� utilise
-- principalement pour la classification dans l'intelligence artificielle. L'idee generale de KNN est que etant donne un
-- echantillon de reference compose de X instances dont on connait deja leur classe, pour une nouvelle instance Y(dont
-- on connait pas sa classe) on associe la classe majoritaire des k instances de r�f�rence les plus proches de la
-- nouvelle entree Y. Dans le cas ou K=1, on associe a Y la meme classe de l'instance de reference la plus proche (la plus similaire).
-- Plus de documentation sur k-Nearest Neighbors : http://en.wikipedia.org/wiki/K-nearest_neighbors_algorithm

-- Creez l'algorithme KNN pour K=1 (version 1NN)
	-- la description d'une instance est sous la forme d'une liste d'entiers (vecteurs) (exemple [1, 1, 2, 2, 1]).
	-- Une instance est de type Knn_data et est representee par le tuplet ([description], sa classe)
	-- (exemple x = ([1, 1, 2, 2, 1], "classe_de_x"))
type Knn_data = ([Integer], String)

	-- a) (2pts) Il faut definir une fonction recursive "euclidean_dist" qui permet de mesurer la similarit�
	-- (selon la distance euclidienne) entre deux vecteurs. Cette fonction retourne la distance euclidienne entre les deux vecteurs
euclidean_calc :: ([Integer],[Integer])->Float
euclidean_calc (x, y) = if x == [] then 0
                        else ((fromIntegral (head  x) - fromIntegral (head y))**2) + euclidean_calc (tail x, tail y)

euclidean_dist :: ([Integer],[Integer])->Float
euclidean_dist (x, y) = if length x /= length y then error "ERREUR : les vecteurs ne sont pas dans la même dimension"
                        else sqrt (euclidean_calc (x, y))

	-- b) (2pts) etant donnee le vecteur representant une instance "y" dont on ne conait pas sa classe, la fonction
	-- recursive "dist_lst" prend en parametre ce vecteur (de y) et la liste d'instances de reference (de type Knn_data),
	-- elle retourne la liste des distances entre "y" et toutes les instances de reference.
dist_lst :: [Integer]->[Knn_data]->[Float]
dist_lst x y = if length y == 1 then [euclidean_dist (x, fst (head y))]
               else [euclidean_dist (x, fst (head y))] ++ dist_lst x (tail y)

	-- c) (2pts) la fonction "knn" represente la fonction principale qui retourne la classe associee a l'instance "y"
	-- passe en parametre (sous la forme de son vecteur de description). La fonction recursive "knn" prend aussi en
	-- parametre la liste d'instances de reference (de type Knn_data). Cette fonction utilise les fonctions "dist_lst"
	-- et/ou "euclidean_dist" pour trouver la classe de l'instance "y"(il faut utiliser au moin une des deux fonctions).
knn::[Integer]->[Knn_data]->String
knn x y = if length y == 1 then snd (head y)
          else if euclidean_dist (x, fst (head y)) > euclidean_dist (x, fst (last y)) then knn x (tail y)
          else knn x (init y)
