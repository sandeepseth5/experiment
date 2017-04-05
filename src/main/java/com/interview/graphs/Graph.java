package com.interview.graphs;

import java.util.ArrayList;

public class Graph {
	private final int V;
	private ArrayList<Integer>[] adj;
	
	public Graph(int V) {
		this.V = V;
		adj = new ArrayList[V];
		for (int i=0;i<V;i++) {
			adj[i] = new ArrayList<Integer>();
		}
	}
	
	public void addEdge(int v, int w) {
		adj[v].add(w);
		adj[w].add(v);
	}
	
	public Iterable<Integer> adj(int v) {
		return adj[v];
	}
	
	public int V() {
		return V;
	}
	
	public static void main(String[] args) {
		Graph g = new Graph(3);
		g.addEdge(0, 1);
		g.addEdge(1, 2);
		g.addEdge(2, 0);
		
		for (int v=0;v<g.V();v++) {
			for (int w:g.adj(v)) {
				System.out.println(v + " - " + w);
			}
		}
		DepthFirstPaths dfs = new DepthFirstPaths(g, 0);
	}
}
