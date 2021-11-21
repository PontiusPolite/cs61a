(define (split-at lst n)
 ; split at returns a list lst where (car lst) = (1 2 3) and (cdr lst) = (4 5 6)
 (cond 
    ; if n is 0, return a list containing nil and lst
    ((zero? n) (cons nil lst))
    ; if we've reached the end of the list, return a list containing nil and nil
    ((null? lst) (cons nil nil))
    ; otherwise, we need to add the first element of the list to our construction
    (else 
      (begin
        (define rec (split-at (cdr lst) (- n 1)))
        (cons (cons (car lst) (car rec)) (cdr rec))
      )      
    )
  )
)

(define (compose-all funcs)
  ; if funcs is empty, return the identity function
  (if (null? funcs) 
    (lambda (x) x)
    (lambda (x) 
      ((compose-all (cdr funcs)) ((car funcs) x))
    )
  )
)

