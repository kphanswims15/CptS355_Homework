(* Kimi Phan *)
(* 11466435  *)
(* Homework 4 *)
(* Mac os/Unix *)

(* 1. exists *)

(* This function returns true if the first argument is a member of the second argument *)

(* if the list for argument 2 is empty then return false *)
fun exists(x, []) = false
	(* if the list is not empty it checks the first element to see if they are the same *)
	| exists(x, y::ys) = if(x = y) then true
							(* if they first element is not equal then it keeps on check
							recursively *)
						   	else exists (x, ys);

(* The type is (''a * ''a list) -> bool and not ('a * 'a list) -> bool because ''a is a
 type variable that can only be substituted by types that support equality testing and in
 this function you are doing a equality testing to see if the element is in the list. *)
		   	
(* 2. listUnion *)

(* listUnion returns the union of two lists. Each value in the output list should appear
only once and order does not matter. The type of the function should be (''a list *
''a list) -> ''a list *)

fun combine(L1, L2) = if null(L1) then L2
						else hd(L1)::combine(tl(L1), L2);
fun delete(x, []) = []
	| delete(x, L2::l) = if x = L2 then delete(x, l) 
								else L2::delete(x, l);
fun removeDup [] = []
	| removeDup(x::l) = x::removeDup(delete(x, l));
		
listUnion(L1, L2) = removeDup(combine(L1, L2));
			
(* 3. listIntersect *)

(* This returns the intersection of two lists and has type ''a list -> ''a list -> ''a 
list *)

	