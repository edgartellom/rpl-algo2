package ejercicio5

type nodoLista[T any] struct {
	prox *nodoLista[T]
	dato T
}

type ListaEnlazada[T any] struct {
	prim *nodoLista[T]
}
