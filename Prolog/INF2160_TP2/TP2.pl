/*
 * MAXIME GRENIER 	: 	GREM17078606
 * DANY DEROY		:	DERD02088403
 */

ajouter_noeud :-
  	write('Donnez la liste des noeuds'), nl,
	repeat,
		write('Donnez l\'index du noeud : '),
		read(Index),
		(		
		noeud(Index,_) -> (write('noeud deja existant'), nl, fail);
		(
		write('Donnez le nom de la personne : '),
		read(Label), nl,
		assert(noeud(Index, Label)),
		write('Voulez vous continuer (oui/non)? '),
		read(Reponse),
		(not(Reponse=oui),!); fail
		)
		).
		
supprimer_noeud :-
	write('Entrer un index a supprimer'), nl,
	read(X),
	(
	retract(noeud(X,Y)),
	write(noeud(X,Y)),
	write('supprime'),
	(
	forall(lien(X,_), retract(lien(X,_))),
	forall(lien(_,X), retract(lien(_,X)))
	),!;
	write('Noeud introuvable'),!
	),nl.

ajouter_lien :-
	repeat,
		write('Donnez la liste des liens'), nl,
		write('donnez l\'index du premier noeud '), nl,
		read(X),
		write('donnez l\'index du deuxième noeud '), nl,
		read(Y),   
		(
		(not(noeud(X,_)); not(noeud(Y,_))) -> (write('noeud introuvable'), nl, fail);
		(
		(lien(X,Y); lien(Y,X)) -> (write('lien deja existant'), nl, fail);
		(   
		assert(lien(X,Y)),
		write('Desirez-vous continuer (oui/non)?'), nl,
		read(Reponse),
		(not(Reponse=oui),!); fail
		))).
		
supprimer_lien :-
   write('Donnez l\'index du premier lien'), nl,
   read(X),
   write('Donnez l\'indez du deuxième lien'), nl,
   read(Y),
   (   
	retract(lien(X,Y)),
	write(lien(X,Y)),
	write(' supprimé');
	write('lien introuvable')
   ),
   nl.

verifier :- 
	(
	lien(_,_) -> lien(A,B), noeud(A,X), noeud(B,Y);
	write('graphe vide')
	),
	(
	X == Y -> write('graphe non valide'); 
	write('graphe valide')
	).

amitie(X,Y) :-
	Y == X,!;
	(
	noeud(Z,X),
	lien(Z,Q),
	noeud(Q,X2),
	amitie(X2,Y),!
	);
	(
	noeud(Z,Y),
	lien(Z,Q),
	noeud(Q,Y2),
	amitie(X,Y2),!
	).
	
	
commun(X,Y,N) :-
	noeud(A,X),
	noeud(B,Y),
	(
	lien(A,AX);
	lien(AX,A)
	),
	(
	lien(BY,B);
	lien(B,BY)
	),
	AX == BY,
	noeud(BY,N).

intermediaires(X,Y,N):- 
	noeud(LX,X),
	noeud(LY,Y),
	lien(LX,LY),
	N is 0.

intermediaires(X,Y,N):- 
	noeud(LX,X),
	noeud(LY,Z),
	lien(LX, LY),
	intermediaires(Z,Y,N1),
	N is N1 + 1.

suggestion(X,Y):-
	intermediaires(X,Y,1);
	intermediaires(X,Y,2).

:- dynamic lien/2.
:- dynamic noeud/2.
