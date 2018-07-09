; Kimi Phan
; ID: 11466435
; Assignment 3 (Scheme)
; Mac os/Unix

; Problem 1 (deepSum)
(define (deepSum L) (cond
                      ((null? L) 0) ; if the list is at the end or if the list is empty
                      ; if the element is a sub list it add up the sublists elements 
                      ((list? (car L)) (+ (deepSum(car L))(deepSum(cdr L))))
                      ; adds up the elements in L 
                      (else (+ (car L)(deepSum(cdr L))))))

; Problem 2 (numbersToSum sum L)
(define (numbersToSum sum L)(cond
                              ; checks if the sum is bigger than the first element in the list then it modifies the sum by subtracting the first element from the sum and it keeps
                              ; going until the sum becomes smaller than the next element
                              ((> sum (car L))(cons (car L)(numbersToSum (- sum (car L)) (cdr L))))
                              ; if the list is empty or there are number in the list returns and empty list
                              (else '())))

; Problem 3 (isSorted L)
(define (isSorted L) (cond
                       ; if it is empty return true
                       ((null? L) #t)
                       ; if the length is 1 the return true
                       ((eq? (length L) 1) #t)
                       ; if element 2 is bigger than element 1 continue checking the list 
                       ((> (car (cdr L))(car L)) (isSorted (cdr L)))
                       ; if element 1 is bigger than element 2 then return false 
                       (else #f)))

; Problem 4 (mergeUnique2 L1 L2)
(define (mergeUnique2 L1 L2) (cond
                               ; if L1 is empty then return L2
                               ((null? L1) L2)
                               ; if L2 is empty then return L1
                               ((null? L2) L1)
                               ; if the first element of L1 is larger than L2 then return the first element in L1
                               ((< (car L1)(car L2))(cons (car L1)(mergeUnique2 (cdr L1) L2)))
                               ; if the first elements in both lists are equal then return return the first element in L1
                               ((= (car L1)(car L2)) (cons (car L1)(mergeUnique2 (cdr L1) (cdr L2))))
                               ; if the first element in L2 is larger then return the first element in L2
                               (else (cons (car L2)(mergeUnique2 L1 (cdr L2))))))

; (fold L)
(define (fold f base L)(cond
                         ((null? L) base)
                         (else (f (car L)(fold f base (cdr L))))))

; Problem 5 (mergeUniqueN Ln)
; mergeUnique2 is the base and it folds an empty list to the rest of the lists merging the two lists using mergeUnique2 
(define (mergeUniqueN Ln)(fold mergeUnique2 '() Ln))

; Problem 6 (matrixMap f M)
(define (matrixMap f M)(cond
                         ; if the matrix is empty it returns and empty list 
                         ((null? M) '())
                         ; maps the function to the first list in the matrix and uses map again to map the function to the second list
                         (else (map (lambda (L) (map f L)) M))))

; Problem 7 (avgOdd L)
; filter
(define (filter pred L) (cond
                          ((null? L) '())
                          ((pred (car L))(cons (car L)(filter pred (cdr L))))
                          (else (filter pred (cdr L)))))

(define (avgOdd L)(cond
                    ; if the list is empty returns an empty list
                    ((null? L) '())
                    ; if there is no odd numbers in the list then the average is zero
                    ((equal? (length (filter odd? L)) 0) 0)
                    ; filters the odd numbers out then adds them together and divides the length of the list to get the average
                    (else (/ (fold + 0 (filter odd? L))(length (filter odd? L))))))


; Problem 8 (unzip)
(define (unzip L)(cond
                   ; if the list is empty it returns an empty list 
                   ((null? L) '())
                   ; unzip pairs into lists. The first cons puts the first elements together and the second part puts the second elements into a list by using lambda and maping list to each element  
                   (else (cons (map car L) (list (map (lambda (l) (car (cdr l))) L))))))

; test cases

;testing deepSum
(display "Testing deepSum")
(newline)
(equal? (deepSum '(1 (2 3 4) (5) 6 7 (8 9 10) 11)) 66)
(equal? (deepSum '()) 0)

;testing numbersToSum
(display "Testing numbersToSum")
(newline)
(equal? (numbersToSum 100 '(10 20 30 40)) '(10 20 30))
(equal? (numbersToSum 30 '(5 4 6 10 4 2 1 5)) '(5 4 6 10 4))
(equal? (numbersToSum 1 ' (10 20 30 40)) '())

; testing isSorted
(display "Testing isSorted")
(newline)
(equal? (isSorted '(1 4 5 6 10)) #t)
(equal? (isSorted '(1 3 6 5 10)) #f)
(equal? (isSorted '(1)) #t)
(equal? (isSorted '()) #t)

; testing mergeUnique2
(display "Testing mergeUnique2")
(newline)
(equal? (mergeUnique2 '(4 6 7) '(3 5 7)) '(3 4 5 6 7))
(equal? (mergeUnique2 '(1 5 7) '(2 5 7)) '(1 2 5 7))
(equal? (mergeUnique2 '() '(3 5 7)) '(3 5 7))
(equal? (mergeUnique2 '() '()) '())
(equal? (mergeUnique2 '(4) '(4)) '(4))
(equal? (mergeUnique2 '(4 5) '(5 6)) '(4 5 6))

; testing mergeUniqueN
(display "Testing mergeUniqueN")
(newline)
(equal? (mergeUniqueN '()) '())
(equal? (mergeUniqueN '((2 4 6) (1 4 5 6))) '(1 2 4 5 6))
(equal? (mergeUniqueN '((2 4 6 10) (1 3 6) (8 9))) '(1 2 3 4 6 8 9 10))

; testing matrixMap
(display "Testing matrixMap")
(newline)
(equal? (matrixMap (lambda (x) (* x x)) '((1 2) (3 4))) '((1 4) (9 16)))
(equal? (matrixMap (lambda (x) (+ 1 x)) '((0 1 2) (3 4 5))) '((1 2 3) (4 5 6)))
(equal? (matrixMap (lambda (x) (+ 1 x)) '(() ())) '(() ()))
(equal? (matrixMap (lambda (x) (* 5 x)) '((0 1 2) (3 4 5))) '((0 5 10) (15 20 25)))
(equal? (matrixMap (lambda (x) (- 1 x)) '((0 1 2) (3 4 5))) '((1 0 -1)(-2 -3 -4)))
(equal? (matrixMap (lambda (x) (/ x 1)) '((1 2 3) (4 5 6))) '((1 2 3)(4 5 6)))

; testing avgOdd
(display "Testing avgOdd")
(newline)
(equal? (avgOdd '(1 2 3 4 5)) 3)
(equal? (avgOdd '(1 2 5)) 3)
(equal? (avgOdd '(1 2 4 6)) 1)
(equal? (avgOdd '()) '())
(equal? (avgOdd '(2 4 6)) 0)

; testing unzip
(display "Testing unzip")
(newline)
(equal? (unzip '((1 2) (3 4) (5 6))) '((1 3 5) (2 4 6)))
(equal? (unzip '((1 "a") (5 "b") (8 "c"))) '((1 5 8)("a" "b" "c")))
(equal? (unzip '()) '())